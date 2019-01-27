from tasks.task5 import *


def test_01_today_date():
    result = check_my_date("27.02.2019")
    assert result == True


def test_02_last_year_date():
    result = check_my_date("27.02.2018")
    assert result == True


def test_03_next_year_date():
    result = check_my_date("27.02.2020")
    assert result == True


def test_04_last_centure_date():
    result = check_my_date("27.02.1982")
    assert result == True


def test_05_next_centure_date():
    result = check_my_date("27.02.2121")
    assert result == True


def test_06_american_format_date():
    result = check_my_date("12.24.2018")
    assert result == True


def test_07_db_format_date():
    result = check_my_date("2018-04-12")
    assert result == True


def test_08_another_formate1_date():
    result = check_my_date("30.09.19")
    assert result == True


def test_09_another_format2_date():
    result = check_my_date("27 apr 2018")
    assert result == True


def test_10_another_format3_date():
    result = check_my_date("April, 12, 1978")
    assert result == True


def test_11_wrong_format1_date():
    result = check_my_date("678687686")
    assert result == False


