import pytest

from pyreqres.models import Login, Register, Users


@pytest.fixture(scope="session")
def pyf_Users() -> Users:
    return Users()


@pytest.fixture(scope="session")
def pyf_Register() -> Register:
    return Register()


@pytest.fixture(scope="session")
def pyf_Login() -> Login:
    return Login()
