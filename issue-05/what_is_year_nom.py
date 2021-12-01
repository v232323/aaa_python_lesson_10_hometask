import urllib.request
import json
from unittest.mock import MagicMock
from unittest.mock import patch

import pytest

API_URL = 'http://worldclockapi.com/api/json/utc/now'

YMD_SEP = '-'
YMD_SEP_INDEX = 4
YMD_YEAR_SLICE = slice(None, YMD_SEP_INDEX)

DMY_SEP = '.'
DMY_SEP_INDEX = 5
DMY_YEAR_SLICE = slice(DMY_SEP_INDEX + 1, DMY_SEP_INDEX + 5)


def what_is_year_now() -> int:
    """
    Получает текущее время из API-worldclock и извлекает из поля 'currentDateTime' год

    Предположим, что currentDateTime может быть в двух форматах:
      * YYYY-MM-DD - 2019-03-01
      * DD.MM.YYYY - 01.03.2019
    """
    with urllib.request.urlopen(API_URL) as resp:
        resp_json = json.load(resp)

    datetime_str = resp_json['currentDateTime']
    if datetime_str[YMD_SEP_INDEX] == YMD_SEP:
        year_str = datetime_str[YMD_YEAR_SLICE]
    elif datetime_str[DMY_SEP_INDEX] == DMY_SEP:
        year_str = datetime_str[DMY_YEAR_SLICE]
    else:
        raise ValueError('Invalid format')

    return int(year_str)


def test_what_is_year_now_mock_json():
    exp_json = {'currentDateTime':'2019-11-30T12:06Z'}
    exp_year = 2019

    with patch('json.load') as mock:
        mock.return_value = exp_json
        year = what_is_year_now()
    assert year == exp_year


def test_what_is_year_now_mock_request():
    exp_json = {'currentDateTime':'2019-11-30T12:06Z'}
    exp_year = 2019

    with patch('urllib.request') as mock:
        mock.urlopen(API_URL).return_value = None
        with patch('json.load') as mock2:
            mock2.return_value = exp_json
            year = what_is_year_now()
        assert year == exp_year


def test_what_is_year_now_mock_another_format():
    exp_json = {'currentDateTime':'01.03.2021'}
    exp_year = 2021

    with patch('json.load') as mock:
        mock.return_value = exp_json
        year = what_is_year_now()
    assert year == exp_year


def test_what_is_year_now_mock_invalid_format():
    exp_json = {'currentDateTime':'privet'}

    with patch('json.load') as mock:
        mock.return_value = exp_json
        with pytest.raises(ValueError):
            year = what_is_year_now()