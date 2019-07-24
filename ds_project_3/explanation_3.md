We can form a maximum number when we have highest number in first place followed by second highest number and so on. Also, We can get highest number on addition of two numbers when both the number are of high range.
for example if we have 1,2,3,4:
adding the numbers in sorted order 43+21 gives 64 where as 42+31 gives: 73
Taken this idea in mind, we first sorted the incoming array. We used merge sort which gives a guarantee of O(n log n ) time complexity.
Now we have modified the original merge sort into giving us an array in descending order

Next we traversed the sorted list to create the two highest numbers by getting alternate numbers.

Time complexity: O(n log n) for merge sort and O(n) to generate highest number. O(nlog n) being dominant , it is the overall complexity
Space: O(n) since we need an array for merge sort
