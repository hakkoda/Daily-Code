# Write a code fragment that prints the contents of a two-dimensional boolean
# array, using * to represent true and a space to represent false.  Include row
# and columns numbers.
#
# Example:
#
# my_list = [ 
#   [ True, False, True ],
#   [ False, True, True ],
#   [ True, True, False ],
# ]
# 
# will become:
# 
#   1 2 3
# 1 *   *
# 2   * *
# 3 * *

def run(boolean_list):
    result = " "
    
    # Setup column header numbers
    for column in range(len(boolean_list[0])):
        result += f" {column+1}"

    for row in range(len(boolean_list)):
        # Add row number to beginning of new line
        result += f"\n{row+1}" 
        for column in range(len(boolean_list[row])):
            # Add '*' for true value, and ' ' for false value
            result += f" *" if boolean_list[row][column] else "  "

    return result;



if __name__ == "__main__":
    result = run([ [True, False, True], [False, True, False] ])
    print(result)

    result = run([ 
        [True,  False, False, False,  True], 
        [False,  True,  True,  True, False],
        [False,  True,  True,  True, False], 
        [False,  True,  True,  True, False], 
        [False,  True,  True,  True, True ] 
    ])
    print(result)

    result = run([ 
        [True]
    ])
    print(result)

    result = run([ 
        [False]
    ])
    print(result)
