# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division

@pytest.mark.parametrize('a, b, result',
    [
    pytest.param(8, 2, 4, marks=pytest.mark.smoke),
    pytest.param(-15, 3, -5, marks=pytest.mark.smoke),
    pytest.param(-8, -2, 4, marks=pytest.mark.skip),
    pytest.param(999, 111, 9, marks=pytest.mark.skip),
    pytest.param(8, 0, ZeroDivisionError)
    ])
def test_all_division_two_param(a, b, result):
    if b == 0:
        with pytest.raises(ZeroDivisionError):
            all_division(8, 0)
    else:
        assert all_division(a, b) == result


