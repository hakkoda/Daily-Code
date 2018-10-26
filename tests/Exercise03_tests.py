from nose.tools import *
from DailyCode.Exercise03 import *

def to_binary_formatted_test():
    test_nums = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 16, 20, 255 ]
    expected_results = [
         "  0: 0000 0000"
        ,"  1: 0000 0001"
        ,"  2: 0000 0010"
        ,"  3: 0000 0011"
        ,"  4: 0000 0100"
        ,"  5: 0000 0101"
        ,"  6: 0000 0110"
        ,"  7: 0000 0111"
        ,"  8: 0000 1000"
        ,"  9: 0000 1001"
        ," 10: 0000 1010"
        ," 15: 0000 1111"
        ," 16: 0001 0000"
        ," 20: 0001 0100"
        ,"255: 1111 1111"
    ]
    results = [to_binary_formatted(num) for num in test_nums]

    for result, expected in zip(results, expected_results):
        assert_equal(result, expected)
