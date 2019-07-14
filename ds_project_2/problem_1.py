
# The cache is implemented by using a combination of dictionary and and doubly linked list. Items are stored in a node format which
# in turn creates the linked list. The head of the liked list points to the most recently used item, whereas the tail item points to least recently
# used item. The hash table provides an efficient way of lookup for the value based on key. Whereas the linked list provide the flexibility of moving
# the most recently used item to the head by just updating the pointers in a constant time.

#The class will help to create the doubly linked list. It store the key, value and the next and prev item
class Node(object):
    def __init__(self,key,value):
        # Initialize class variables
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

#The class implements the actual LRU algorithm
class LRU_Cache(object):

    def __init__(self, capacity):
        '''
            Initialize class variables
        '''
        # capture the overall capacity
        self.capacity = capacity
        # Maintains the cache for constant time lookup
        self.cache = {}
        # holds the current size of the cache
        self.size = 0
        # points to the most recently used item
        self.head = None
        # points to the least recently used item
        self.tail = None


    def get(self, key):
        '''
            Retrieve item from provided key. Return -1 if nonexistent.
        '''
        # if the key is not present in cache, return -1
        if key not in self.cache:
            return -1
        # retrieve the node from the key
        node = self.cache[key]

        # Since the node has been accessed remove the node from its current position and add it to the head to signify, it has been recently used.
        # Perform the operation only if the node is not already the head
        if self.head != node:
            self.__remove(node)
            self.__set_head(node)

        # return the value
        return node.value



    def set(self, key, value):
        '''
            Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        '''
        if self.capacity == 0 or self.capacity is None:
            return None
        # check if the key already exist in cache. Then update the value. Also remove the node from its current position
        # and add it to the head to signify, it has been recently used,
        # only if the node is not already the head
        if key in self.cache:
            node = self.cache[key]
            node.value = value

            if self.head != node:
                self.__remove(node)
                self.__set_head(node)
        # if the key is not present, then create a new node and add it to the cache and also set the head to the new node, to signify it has been used recently.
        # before insertion , we need to check the capacity is not full, if full then remove the tail entry(least recently used) before making an entry
        else:
            new_Node = Node(key,value)
            if self.__is_capacity_full():
                del self.cache[self.tail.key]
                self.__remove(self.tail)
            self.__set_head(new_Node)
            self.cache[key] = new_Node


    def __set_head(self,node):
        '''
            Set the head as the new node passed
        '''
        # if head is not set yet, then set both head and tail to the new node
        if self.head is None:
            self.head = node
            self.tail = node
        # if head is set, then set the current head as previous of new node, new node next to current head before setting the new node as head
        else:
            node.prev = self.head
            self.head.next = node
            self.head = node
        # increase the size
        self.size += 1

    def __remove(self,node):
        '''
            Remove the Node from the current least recently used list
        '''

        # if head is not set then do nothing
        if self.head is None:
            return

        # break the link between other nodes and the input node by updating the prev and/or next link.
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev

        # if the input node is tail, then update the tail to point to next element
        if self.tail == node:
            self.tail = node.next
            self.tail.prev = None
        # decrease the size and return the node
        self.size -= 1
        return node

    def __is_capacity_full(self):
        '''
            Check if the cache has reached its full capacity
        '''
        return self.size == self.capacity

# create cache
our_cache = LRU_Cache(5)
#check cache before adding
print(our_cache.get(1))
#return -1

#add values
our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);
# after adding lru list::: 1<->2<->3<->4

print(our_cache.get(1))
# 1
# after adding lru list::: 2<->3<->4<->1
print(our_cache.get(2))
# 2
# after adding lru list::: 3<->4<->1<->2
print(our_cache.get(9))
# -1
# because 9 is not present in the cache
# after adding lru list::: 3<->4<->1<->2

our_cache.set(5, 5)
# after adding lru list::: 3<->4<->1<->2<->5
our_cache.set(6, 6)
# after adding lru list::: 4<->1<->2<->5<->6
# remove 3 since it is least recently used and max capacity reached


print(our_cache.get(3))
# -1
# because the cache reached it's capacity and 3 was the least recently used entry
print(our_cache.get(6))
# 6
# after adding lru list::: 4<->1<->2<->5<->6
print(our_cache.get(5))
# 5
# after adding lru list::: 4<->1<->2<->6<->5
print(our_cache.get(4))
# 4
# after adding lru list::: 1<->2<->6<->5<->4
our_cache.set(7, 7);
# after adding lru list::: 2<->6<->5<->4<->7
# remove 1 since it is least recently used and max capacity reached
print(our_cache.get(1))
# -1
# because the cache reached it's capacity and 3 was the least recently used entry
our_cache.set(7, 'seven');
# after adding lru list::: 2<->6<->5<->4<->7
# modifying its value
print(our_cache.get(7))
#seven

none_cache = LRU_Cache(0)
print(none_cache.get(1))
# -1
# since cache doesn't have anything
none_cache.set(1,1)
#does nothing
print(none_cache.get(1))
# -1
# since cache doesn't have anything
