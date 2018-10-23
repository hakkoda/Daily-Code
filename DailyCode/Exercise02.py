# Write a program that takes three integer command line arguments and prints
# equal if all three are equal, and not equal otherwise
from sys import argv

def get_args():
    result = argv[1:]
    return result

def check_equal(args):
    if len(args) == 3:
        if args[0] == args[1]:
            if args[1] == args[2]:
                return True
    return False

def run():
    args = get_args()
    return check_equal(args)

if __name__ == "__main__":
    result = run()
    print(f"result: {result}")
