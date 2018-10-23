from nose.tools import *
from DailyCode.Exercise02 import check_equal

def check_equal_true_test():
    args = [1,1,1]
    result = check_equal(args)
    assert_equal(result, True)

def check_equal_false_test():
    args = [1,2,3]
    result = check_equal(args)
    assert_equal(result, False)

def check_equal_not_enough_args_test():
    args = [1]
    result = check_equal(args)
    assert_equal(result, False)
