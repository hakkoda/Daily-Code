# Write a code fragment that puts the binary representation of a positive
# integer N into a String s.

#  0 --> 0000 0000
#  1 --> 0000 0001
#  2 --> 0000 0010
#  3 --> 0000 0011
#  4 --> 0000 0100
#  5 --> 0000 0101
# 10 --> 0000 1010
# 20 --> 0001 0100

# TODO: unit tests, format output more nicely


def to_binary(start_x):
    remainder_x = int(start_x / 2)
    mod_x = start_x % 2

    if remainder_x > 0:
        return to_binary(remainder_x) + format("{0}".format(mod_x))
    else:
        return format("{0}".format(mod_x))

print(to_binary(1))
print(to_binary(2))
print(to_binary(3))
print(to_binary(4))
print(to_binary(5))
print(to_binary(6))
print(to_binary(7))
print(to_binary(8))
print(to_binary(9))
print(to_binary(10))
