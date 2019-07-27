We are using binary search to search the value. if the array has been rotated, still the subarrays will be sorted. we need to determine that subarray. so for every iteration:
case 1: if mid index value is equal to number being searched, return the index
case 2: We are checking if right side is sorted or if left side is unsorted. if so we check if number is greater than mid and less than end: number is in right side else left side
case 3: We are checking if left side is sorted or right side is unsorted. if so  we check if number is less than mid and greater than start: number is in left side else right side
case 4: if number doesn't fall in above ranges, increase start by 1

The overall complexity, is O(log n)
Space complexity: O(1), since we are using temp variables for calculation.
