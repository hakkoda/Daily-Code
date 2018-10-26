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

# TODO: unit tests

def to_binary(num):
    quotient = int(num / 2)
    mod = num % 2

    if quotient > 0:
        return to_binary(quotient) + str(mod)
    else:
        return str(mod)

def to_binary_formatted(num):
    binary = to_binary(num)
    binary = binary.rjust(8, "0")
    binary = binary[0:4] + " " + binary[4:8]
    return f"{str(num).rjust(3)}: {binary}"


print(to_binary_formatted(0))
print(to_binary_formatted(1))
print(to_binary_formatted(2))
print(to_binary_formatted(3))
print(to_binary_formatted(4))
print(to_binary_formatted(5))
print(to_binary_formatted(6))
print(to_binary_formatted(7))
print(to_binary_formatted(8))
print(to_binary_formatted(9))
print(to_binary_formatted(10))
print(to_binary_formatted(15))
print(to_binary_formatted(16))
print(to_binary_formatted(20))
print(to_binary_formatted(255))
