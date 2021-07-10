import pytest
from decimal import  *

from session9 import profiles_summary_named_tuples, profiles_summary_dict, stock_market

def test_profiles_named_tuples():
    mean_age, oldest, lat, lng, max_bt, time_elapsed = profiles_summary_named_tuples(10000)

    assert mean_age >= 57 and mean_age <= 58
    assert oldest == 115
    # assert str(lat) == "-0.3332624775"
    # assert str(lng) == "1.3958205756"
    assert float(lat) <= 5 and float(lat) >= -5
    assert float(lng) <= 5 and float(lng) >= -5
    assert max_bt == "AB+"
    assert time_elapsed < 3


def test_profiles_dict():
    mean_age, oldest, lat, lng, max_bt, time_elapsed = profiles_summary_dict(10000)

    assert mean_age >= 57 and mean_age <= 58
    assert oldest == 115
    # assert str(lat) == "-0.3332624775"
    # assert str(lng) == "1.3958205756"
    assert float(lat) <= 5 and float(lat) >= -5
    assert float(lng) <= 5 and float(lng) >= -5
    assert max_bt == "AB+"
    assert time_elapsed < 3


def test_profiles_dict2():
    mean_age, oldest, lat, lng, max_bt, time_elapsed_nt = profiles_summary_named_tuples(10000, False)
    mean_age, oldest, lat, lng, max_bt, time_elapsed_d = profiles_summary_dict(10000, False)

    print("\n==========Comparision test:")
    print("named tuple time=", time_elapsed_nt, ", dict time: ", time_elapsed_d )
    assert time_elapsed_nt < time_elapsed_d


def test_stock_exchange():
    open, close, mean_open, mean_close, high = stock_market(1000)
    print(open, close, mean_open, mean_close, high)
    difference = abs(mean_open - mean_close)
    assert difference <= 1000