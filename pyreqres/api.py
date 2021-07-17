import json

import requests
from requests.exceptions import HTTPError, RequestException

from pyreqres.utils.pkg_log import logger

__all__ = ["GET", "POST", "PUT", "PATCH", "DELETE"]


def GET(url: str, timeout=60, **query_params):
    try:
        response = requests.get(url, timeout=timeout, params=query_params)
        response.raise_for_status()
        logger.info("Calling URL {} Successful".format(response.url))
        return response
    except HTTPError as http_error:
        logger.warning(
            "HTTPError during Request for URL {}. Error Details - {}".format(
                response.url, http_error
            )
        )
        return response
    except RequestException as reqexc:
        raise Exception(f"Something went wrong...More Details\n{reqexc}.")


def DELETE(url: str, timeout=60):
    try:
        response = requests.delete(url, timeout=timeout)
        response.raise_for_status()
        logger.info("Calling URL {} Successful".format(response.url))
        return response
    except HTTPError as http_error:
        logger.warning(
            "HTTPError during Request for URL {}. Error Details - {}".format(
                response.url, http_error
            )
        )
        return response
    except RequestException as reqexc:
        raise Exception(f"Something went wrong...More Details\n{reqexc}.")


def _UPDATE(update_method: str, url: str, timeout: int = 60, **update_data):
    if update_method.lower() == "post":
        __update_request = requests.post
    elif update_method.lower() == "put":
        __update_request = requests.put
    elif update_method.lower() == "patch":
        __update_request = requests.patch
    else:
        raise ValueError(
            "Invalid Update Method provided. Valid values are POST, PUT, PATCH"
        )

    try:
        response = __update_request(url, timeout=timeout, data=update_data)
        response.raise_for_status()
        logger.info("Calling URL {} Successful".format(response.url))
        return response
    except HTTPError as http_error:
        logger.warning(
            "HTTPError during Request for URL {}. Error Details - {}".format(
                response.url, http_error
            )
        )
        return response
    except RequestException as reqexc:
        raise Exception(f"Something went wrong...More Details\n{reqexc}.")


def POST(url: str, timeout=60, **data):
    return _UPDATE(update_method="POST", url=url, timeout=timeout, **data)


def PUT(url: str, timeout=60, **data):
    return _UPDATE(update_method="PUT", url=url, timeout=timeout, **data)


def PATCH(url: str, timeout=60, **data):
    return _UPDATE(update_method="PATCH", url=url, timeout=timeout, **data)
