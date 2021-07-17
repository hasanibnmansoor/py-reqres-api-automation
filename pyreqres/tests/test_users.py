from pathlib import Path

import pytest
from requests import codes

from pyreqres.utils import logger, parse_json_file

test_data_file_path = (Path(__file__).parent).joinpath("data/userdata.json")
logger.info(f"Parsing Json Test Data File located at {test_data_file_path}")
test_data = parse_json_file(test_data_file_path)


@pytest.mark.parametrize(
    "_test_data", test_data.list_users.values(), ids=test_data.list_users.keys()
)
def test_list_users(pyf_Users, _test_data):
    """Test Retrieving list of users"""
    users = pyf_Users.list_users(
        page_number=_test_data[0],
        result_per_page=_test_data[1],
    )
    assert users.status == codes.ok  # 200
    assert len(users.body["data"]) == _test_data[2]


def test_valid_get_user(pyf_Users):
    """Test retrieving a valid user"""
    user = pyf_Users.get_user(test_data.user_ids["valid"])
    assert user.status == codes.ok  # 200
    assert user.body["data"]["id"] == test_data.user_ids["valid"]


def test_invalid_get_user(pyf_Users):
    """Test getting invalid user id"""
    user = pyf_Users.get_user(test_data.user_ids["invalid"])
    assert user.status == codes.not_found  # 400


def test_create_user(pyf_Users):
    """Test Create User (POST)"""
    new_user = pyf_Users.create_user(**test_data.create_user)
    assert new_user.status == codes.created  # 201
    assert test_data.create_user.items() <= new_user.body.items()


def test_update_user_put(pyf_Users):
    """Testing Update User data using PUT method"""
    updated_user = pyf_Users.update_user_put(
        test_data.user_ids["valid"], **test_data.put_user
    )
    assert updated_user.status == codes.ok  # 200
    assert test_data.put_user.items() <= updated_user.body.items()


def test_update_user_patch(pyf_Users):
    """Testing Update User data using PATCH method"""
    updated_user = pyf_Users.update_user_patch(
        test_data.user_ids["valid"], **test_data.patch_user
    )
    assert updated_user.status == codes.ok  # 200
    assert test_data.patch_user.items() <= updated_user.body.items()


@pytest.mark.parametrize(
    "user_id",
    [
        test_data.user_ids["valid"],
        test_data.user_ids["invalid"],
    ],
    ids=("existing_user_delete", "non_existing_user_delete"),
)
def test_delete_user(pyf_Users, user_id):
    """Verify Delete User for Existing and Non-Existing User"""
    delete_status = pyf_Users.delete_user(user_id)
    assert delete_status == codes.no_content  # 204
