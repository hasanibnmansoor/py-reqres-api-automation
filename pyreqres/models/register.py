from collections import namedtuple
from typing import Union

from pyreqres import logger
from pyreqres.api import POST

__all__ = ["Register"]

RegisterResponse = namedtuple("Response", "status body")


class Register:
    def __init__(self):
        self._base_url = "https://reqres.in/api/register"

    def register_user(
        self, email: Union[str, None] = None, password: Union[str, None] = None
    ) -> RegisterResponse:
        """POST Method to Register User

        Args:
            email: str | None.
            password: str | None.
        Returns:
            RegisterResponse object
        """
        data = {}
        if email is not None:
            data["email"] = email
        if password is not None:
            data["password"] = password
        logger.info(f"[Request INFO]: Url: {self._base_url}; Data: {data}")
        response = POST(self._base_url, **data)
        return RegisterResponse(response.status_code, response.json())
