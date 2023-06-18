import inspect
import sys

import pytest


def plus(a, b):
    # if not a and not b:
    #     raise ValueError('bad params')
    return a + b

def test1():
    assert plus(2, 2) == 4


def test2():
    assert plus(100, 9) == 108, 'Неверный результат'


def test3():
    assert plus(-1, 1) == 0


def test_zero():
    with pytest.raises(ValueError):
        plus(0, 0)

# g = globals().copy()
# exists_errors = False
# for k, v in g.items():
#     if k.startswith('test') and inspect.isfunction(v):
#         try:
#             print(f'exec {k}')
#             v()
#             print(f'SUCCESS {k}')
#         except Exception as err:
#             exists_errors = True
#             print(err)
#             print(f'FAILED {k} {err}')
#
# if exists_errors:
#     sys.exit(1)
