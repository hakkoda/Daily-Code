[[index|HOME]]

= RECURSION =

There are 3 important rules of thumb in developing recursive program:

1. The recursion has a _base case_ - always include a conditional statement as
   the first statement in the program that has a return.
2. Recursive calls must address sub problems that are _smaller_ in some sense, so
   that recursive calls converge to the base case.  
3. Recursive calls should not address sub problems that _overlap_.  

----

Example for using recursion to perform a binary search.

{{{python
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
}}}
