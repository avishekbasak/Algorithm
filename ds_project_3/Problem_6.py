
def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """

    if not ints or len(ints)<1:
        return ()
    max_val = -float('inf')
    min_val = float ('inf')

    for num in ints:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num
    return (min_val , max_val)

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
#Pass
l=[-9839,123,0,-98,1930]
print ("Pass" if ((-9839, 1930) == get_min_max(l)) else "Fail")
#Pass

l= None
print ("Pass" if (() == get_min_max(l)) else "Fail")
#Pass

l= [-2873]
print ("Pass" if ((-2873,-2873) == get_min_max(l)) else "Fail")
#Pass
