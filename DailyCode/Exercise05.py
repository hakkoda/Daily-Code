# Write a static method histogram() that takes an array a[] of int values and an
# integer M as arguments and returns an array of length M whose ith entry is the
# number of times the integer i appeared in the argument array.  If the values
# in a[] are all between 8 and M-1, the sum of the values in the returned array
# should be equal to a.length.
#
# Example:
# array: [ 0, 1, 2, 3, 0, 1, 2, 3 ]
# M: 4
# result: [ 2, 2, 2, 2 ]
# sum of values in result = 8, array length = 8


def run(num_list, m):
    result = []

    num_count = 0
    for i in range(m):
        num_count = 0
        for num in num_list:
            if num == i:
                num_count += 1
        result.append(num_count)

    return result
