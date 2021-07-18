import random
import pytest
import requests

import random_data


def test_russian_name_male():
    assert isinstance(random_data.russian.names.male(), str)


def test_russian_name_female():
    assert isinstance(random_data.russian.names.female(), str)


@pytest.mark.parametrize("password_length", [
    (random.randint(10, 100))
    for _ in range(random.randint(1, 10))
])
def test_length_password_10(password_length):
    password = random_data.etc.password(length=password_length)
    assert password_length == len(password)


def test_uuid():
    assert isinstance(random_data.etc.uuid(), str)


def test_user_agent():
    assert isinstance(random_data.etc.user_agent(), str)


def test_ip_address():
    for _ in range(5):
        ip_address = random_data.etc.ip_address(check_on_valid=True)
        url = "http://ip-api.com/json/{}".format(ip_address)
        status = requests.get(url).json()["status"]
        assert "success" == status
