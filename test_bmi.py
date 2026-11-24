import pytest

from day03_bmi import calc_bmi

@pytest.mark.parametrize(["height", "weight", "expected"],[
    (1.65, 50.36, "偏瘦"),
    (1.65, 50.37, "正常"),
    (1.65, 65.34, "超重"),
    (1.65, 76.23, "肥胖")])
def test_bmi_level(height,weight,expected):
    assert calc_bmi(height,weight)[1] == expected


def test_偏瘦():
    assert calc_bmi(1.65, 50.36)[1] == "正常"

def test_正常():
    assert calc_bmi(1.65, 50.37)[1] == "正常"

def test_身高为零():
    with pytest.raises(ZeroDivisionError):
        calc_bmi(0, 50)