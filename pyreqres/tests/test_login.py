from pathlib import Path

from requests import codes

from pyreqres import logger, parse_json_file

test_data_file_path = (Path(__file__).parent).joinpath("data/logindata.json")
logger.info(f"Parsing Json Test Data File located at {test_data_file_path}")
test_data = parse_json_file(test_data_file_path)


def test_valid_login(pyf_Login):
    """Verify Successful Login on providing valid username and password.

    Successful Login is determined by Response with Status Code 200
    """
    response = pyf_Login.login_user(
        email=test_data.valid_login["email"],
        password=test_data.valid_login["password"],
    )
    assert response.status == codes.ok  # 200
    assert (
        sorted(response.body.keys()) == test_data.valid_login["response_fields"]
    ), f'Expected Fields {test_data.valid_login["response_fields"]}, but got {response.body.keys()}'


def test_no_email_login(pyf_Login):
    """Verify Error Message on trying to login without username provided.

    Return Status Code: 400
    """
    response = pyf_Login.login_user(password=test_data.no_email_login["password"])
    assert response.status == codes.bad_request  # 400
    assert response.body == test_data.no_email_login["expected_error_message"]


def test_no_password_login(pyf_Login):
    """Verify Error Message on trying to login without password provided.

    Return Status Code: 400
    """
    response = pyf_Login.login_user(email=test_data.no_password_login["email"])
    assert response.status == codes.bad_request  # 400
    assert response.body == test_data.no_password_login["expected_error_message"]


def test_blank_data_login(pyf_Login):
    """Verify Error Message on trying to login with blank data provided.

    Return Status Code: 400
    """
    response = pyf_Login.login_user()
    assert response.status == codes.bad_request  # 400
    assert response.body == test_data.no_email_login["expected_error_message"]


def test_invalid_login(pyf_Login):
    """Verify Error Message on trying to login with an invalid username.

    Return Status Code: 400
    """
    response = pyf_Login.login_user(
        email=test_data.invalid_user_login["email"],
        password=test_data.invalid_user_login["password"],
    )
    assert response.status == codes.bad_request  # 400
    assert response.body == test_data.invalid_user_login["expected_error_message"]
