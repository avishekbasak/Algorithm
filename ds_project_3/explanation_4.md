We followed the below algorithm(since 0s has to be in beginning , 1s in middle and 2s at the end):
1. We defined three pointers, first that points to the start of list, second that points to end of list and third to keep track of the current position
2. Since we have three values, we took 1 as pivot, since we have to over all zero in front of it and all 2's after it
3. if current value as per the third pointer is less than pivot(1), that means we need to swap start element (since all zero has to move forward) with current index. We increment both start and current index.
4. if current value as per the third pointer is more than pivot(1), that means we need to swap end element(since all 2 has to move towards end) with current index. We only decrement end pointer. We do-not modify current index, since we need to check if its less than pivot or it is equal to pivot.
5. if current value as per the third pointer is equal to pivot, we need to move to the next position.

Time complexity: O(n), since we have to iterate the complete List
Space: O(1), since we need space for storing index and pivot
