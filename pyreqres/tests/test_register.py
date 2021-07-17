from pathlib import Path

from requests import codes

from pyreqres import logger, parse_json_file

test_data_file_path = (Path(__file__).parent).joinpath("data/registerdata.json")
logger.info(f"Parsing Json Test Data File located at {test_data_file_path}")
test_data = parse_json_file(test_data_file_path)


def test_valid_registration(pyf_Register):
    """Test for Valid Registration"""
    response = pyf_Register.register_user(
        email=test_data.valid_registration["email"],
        password=test_data.valid_registration["password"],
    )
    assert response.status == codes.ok  # 200
    assert (
        sorted(response.body.keys()) == test_data.valid_registration["response_fields"]
    )


def test_no_email_registration(pyf_Register):
    """Test for Registration without providing an email address"""
    response = pyf_Register.register_user(
        password=test_data.no_email_registration["password"]
    )
    assert response.status == codes.bad_request  # 400
    assert response.body == test_data.no_email_registration["expected_error_message"]


def test_no_password_registration(pyf_Register):
    """Test for Registration without providing a password"""
    response = pyf_Register.register_user(
        email=test_data.no_password_registration["email"]
    )
    assert response.status == codes.bad_request  # 400
    assert response.body == test_data.no_password_registration["expected_error_message"]


def test_blank_data_registration(pyf_Register):
    """Test for Registration without providing an email address & an associated password"""
    response = pyf_Register.register_user()
    assert response.status == codes.bad_request  # 400
    assert response.body == test_data.no_email_registration["expected_error_message"]
