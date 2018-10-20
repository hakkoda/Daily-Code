class BinarySearch(object):
    #def __init__(BinarySearch):
    #    pass

    def rank1(key, values):
        return BinarySearch.rank2(key, values, 0, len(values) - 1)

    def rank2(key, values, lo, hi):
        if lo > hi:
            return -1
        
        mid = int(lo + (hi - lo) / 2)
        if key < values[mid]:
            return BinarySearch.rank2(key, values, lo, mid - 1)
        elif key > values[mid]:
            return BinarySearch.rank2(key, values, mid + 1, hi)
        else:
            return mid


if __name__ == "__main__":
    my_values = [1,2,3,4,5]
    result = BinarySearch.rank1(3, my_values)
    print(f"result: {result}")

# python has no method overloading
# calling static method within a python class seems a little awkward 
# create a test case
