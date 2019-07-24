def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    # return number if its 0 or 1 since 0*0=0 and 1*1=1
    if number == 0 or number ==1:
        return number
    #square root negative number is not real number
    if number < 0:
        return None

    #using binary search, if s is square root of y that means 0<=s<=y. That is
    #s*s = y. if for a given number x, x*x > y that means square root s should lie
    #between 0<=s<x. if for a given number x, x*x < y that means square root s should lie
    #between x<s<=y
    start = 1
    end = number
    floor_sqrt = 0
    iterate=0
    while(start <= end):
        iterate+=1
        #start with middle elemment
        mid = (start + end )//2
        #check if mid * mid = number, then mid is answer
        if mid * mid == number:
            return mid
        #if mid * mid < number, check between range (mid,end]
        #also maintain mid value since, we have to return floor value
        if mid * mid < number:
            start = mid + 1
            floor_sqrt = mid
        #if mid * mid > number, check between range [start,end)
        else:
            end = mid - 1
    return floor_sqrt

print ("Pass" if  (3 == sqrt(9)) else "Fail")
#Pass
print ("Pass" if  (0 == sqrt(0)) else "Fail")
#Pass
print ("Pass" if  (4 == sqrt(16)) else "Fail")
#Pass
print ("Pass" if  (1 == sqrt(1)) else "Fail")
#Pass
print ("Pass" if  (5 == sqrt(27)) else "Fail")
#Pass
print ("Pass" if  (1 == sqrt(3)) else "Fail")
#Pass
print ("Pass" if  (None == sqrt(-3)) else "Fail")
#Pass
