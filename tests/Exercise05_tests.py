from nose.tools import *
from DailyCode.Exercise05 import *

def run_test():
    test_array = [ 0, 1, 2, 3, 0, 1, 2, 3 ]
    m = 4

    result = run(test_array, m)

    test_array_sum = 0
    for x in result:
        test_array_sum += x

    assert_equal(result, [ 2, 2, 2, 2 ])
    assert_equal(len(result), 4)
    assert_equal(test_array_sum, 8)
