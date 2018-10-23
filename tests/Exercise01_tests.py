from nose.tools import *
from DailyCode.Exercise01 import transposition

def transposition_test():
    target_list = [
        [ 1, 1, 1 ],
        [ 2, 2, 2 ],
        [ 3, 3, 3 ],
    ]

    result = transposition(target_list)

    expected_list = [
        [ 1, 2, 3 ],
        [ 1, 2, 3 ],
        [ 1, 2, 3 ],
    ]

    assert_equal(result, expected_list)
