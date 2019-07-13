The cache is implemented by using a combination of dictionary and and doubly linked list. Items are stored in a node format which in turn creates the linked list. The head of the liked list points to the most recently used item, whereas the tail item points to least recently used item. The hash table provides an efficient way of lookup for the value based on key. Whereas the linked list provide the flexibility of moving the most recently used item to the head by just updating the pointers in a constant time.

Time complexity:
Get::
  1. since we are using dictionary for lookup, we can safely say it will be O(1).(Although based on the hash function, if it points to same bucket, it might become O(n))
  2. Since we need to update the link list to make it the head, modification of pointers happens in a constant time, (since we do not have to iterate to find the node).
  3. So overall time complexity can be safely be said as O(1)

Set::
  1. since we are using dictionary for storing, we can safely say it will be O(1).(Although based on the hash function, if it points to same bucket, it might become O(n))
  2. Since we need to update the link list to make it the head, modification of pointers happens in a constant time, (since we do not have to iterate to find the node).
  3. If the capapcity is reached to the max, then we have to update the list to remove the tail element, which again happens in a constant time
  4. So overall time complexity can be safely be said as O(1)

Space complexity:
  1. We definitely need space based on the capacity of the LRU our_cache
  2. But in addition to that we need extra space to maintain the head, tail and prev and next pointer. which is constant. lets say K
  3. So overall space complexity O(n+k), where n is initial capapcity and k is extra space required for the pointers.
