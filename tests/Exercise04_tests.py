from nose.tools import *
from DailyCode.Exercise04 import *

def run_test():
    test_list = [ 
        [ True, False, True ],
        [ False, True, True ],
        [ True, True, False ],
    ]

    expected_result = ""
    expected_result += "  1 2 3\n"
    expected_result += "1 *   *\n"
    expected_result += "2   * *\n"
    expected_result += "3 * *  "

    result = run(test_list)

    assert_equal(result, expected_result)
