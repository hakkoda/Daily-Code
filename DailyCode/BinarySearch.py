class BinarySearch(object):
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


# REVIEW: python has no method overloading?
# REVIEW: how to create/use static methods in python, what are the conventions
# REVIEW: what are the conventions on class names, file names in python?
