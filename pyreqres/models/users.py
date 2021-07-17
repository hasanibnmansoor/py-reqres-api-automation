from collections import namedtuple

from pydantic import validate_arguments

from pyreqres import logger
from pyreqres.api import DELETE, GET, PATCH, POST, PUT

__all__ = ["Users"]

UserResponse = namedtuple("Response", "status body")


class Users:
    def __init__(self):
        self._base_url = "https://reqres.in/api/users"

    @validate_arguments
    def list_users(
        self,
        page_number: int = 1,
        result_per_page: int = 1,
        required_delay_in_seconds: int = 0,
    ) -> UserResponse:
        """GET Method to List all users

        Args:
            page_number: int.
            result_per_page: int To specify number of records to be fetched in data container
            required_delay_in_seconds: int To simulate delay in request.
        Returns:
            UserResponse object
        """
        query_parameters = {
            "page": page_number,
            "per_page": result_per_page,
            "delay": required_delay_in_seconds,
        }
        logger.info(
            f"[Request INFO]: Url: {self._base_url}; Query Parameters: {query_parameters}"
        )
        response = GET(self._base_url, **query_parameters)
        return UserResponse(response.status_code, response.json())

    @validate_arguments
    def get_user(self, user_id: int) -> UserResponse:
        """Get User

        Args:
            user_id: int ID of the user to fetch details
        Returns:
            UserResponse object
        """
        url_ = self._base_url + "/" + str(user_id)
        logger.info(f"[Request INFO]: Url: {url_}")
        response = GET(url_)
        return UserResponse(response.status_code, response.json())

    def create_user(self, **data) -> UserResponse:
        """POST Method to Create User

        Args:
            Any number of Key Value Pair could be passed.
        Returns:
            UserResponse object
        """
        logger.info(f"[Request INFO]: Url: {self._base_url}; Data: {data}")
        response = POST(self._base_url, **data)
        return UserResponse(response.status_code, response.json())

    def update_user_put(self, user_id: int, **data) -> UserResponse:
        """Method to update user data by PUT method

        Args:
            user_id: int User ID to update
            **kwargs: multiple key-value pairs. Data to be sent to update call.
        Returns:
            UserResponse object
        """
        url_ = self._base_url + "/" + str(user_id)
        logger.info(f"[Request INFO]: Url: {url_}; Data: {data}")
        response = PUT(url_, **data)
        return UserResponse(response.status_code, response.json())

    def update_user_patch(self, user_id: int, **data) -> UserResponse:
        """Method to update user data by PATCH method

        Args:
            user_id: int User ID to update
            **kwargs: multiple key-value pairs. Data to be sent to update call.
        Returns:
            UserResponse object
        """
        url_ = self._base_url + "/" + str(user_id)
        logger.info(f"[Request INFO]: Url: {url_}; Data: {data}")
        response = PATCH(url_, **data)
        return UserResponse(response.status_code, response.json())

    @validate_arguments
    def delete_user(self, user_id: int) -> int:
        """Method to DELETE the user

        Args:
            user_id: int ID of the User to delete
        Returns:
            Status Code (expected 204)
        """
        url_ = self._base_url + "/" + str(user_id)
        logger.info(f"[Request INFO]: Url: {url_}")
        response = DELETE(url_)
        return response.status_code
