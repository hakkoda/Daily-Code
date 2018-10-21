from nose.tools import *
from DailyCode.BinarySearch import BinarySearch

# Find the index of 3 in the list, expecting the index result to be 2 (the
# position of 3 in the list.
def rank1_test():
    target_list = [1,2,3,4,5]
    result = BinarySearch.rank1(3, target_list)
    assert_equal(result, 2)
