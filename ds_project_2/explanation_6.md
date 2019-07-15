For union, i iterated both the list at the same time and keep on adding to the result. The loop breaks whenever we reach the end of either list in input. Then we iterate rest of the elements in the other list and add them to result list.

For Intersection, i iterated one list and added them to the set. Then we iterate the second list and check if the value is present in the first set

Time Complexity: for Union it will be O(n) where n is the size of longest linked list.
                  for intersection: it will be O(n+m) where n and mm are the sizes of  both list

Space Complexity: for union it will be O(n), where n is the total unique elements between two list
for intersection it will be O(n+k), where n is the total  elements in first list and k is the total number of common elements
