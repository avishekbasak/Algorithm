If s is square root of Y (s*s =Y) that means 0<=s<=y.
If for a given number x, x*x > y that means square root s should lie between 0<=s<x.
If for a given number x, x*x < y that means square root s should lie between x<s<=y.

Keeping above thought process in mind, and since we have to search in O(log n) time,
so best way to do so is using binary search, where for every pivot element, instead of checking
it is equal to  the number, we are checking pivot * pivot is equal to the number.

The overall complexity, is O(log n)
Space complexity: O(1), since we are using temp variables for calculation.
