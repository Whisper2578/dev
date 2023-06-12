# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

import pytest

def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division

@pytest.mark.smoke
def test_div():
    assert all_division(8, 2) == 4

@pytest.mark.smoke
def test_div_negative_1():
    assert all_division(-15, 3) == -5

@pytest.mark.acceptance
def test_div2():
    assert all_division(8, 2, 2, 2) == 1

@pytest.mark.acceptance
def test_div3():
    with pytest.raises(ZeroDivisionError):
        all_division(8, 0)

@pytest.mark.acceptance
def test_div_negative_2():
    assert all_division(-8, -2) == 4