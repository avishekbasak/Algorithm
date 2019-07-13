class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    temp=set()
    current_1 = llist_1.head
    current_2 = llist_2.head
    result = LinkedList()
    i=0
    if llist_1.size() == 0 and llist_2.size() == 0:
        return None
    elif llist_1.size() == 0:
        return llist_2
    else:
        return llist_1

    while current_1 and current_2:
        if current_1.value not in temp:
            result.append(current_1.value)
            temp.add(current_1.value)
            current_1 = current_1.next
        else:
            current_1 = current_1.next
        if current_2.value not in temp:
            result.append(current_2.value)
            temp.add(current_2.value)
            current_2 = current_2.next
        else:
            current_2 = current_2.next

    if current_1 is not None:
        while current_1 is not None:
            if current_1.value not in temp:
                result.append(current_1.value)
            current_1 = current_1.next

    if current_2 is not None:
        while current_2 is not None:
            if current_2.value not in temp:
                result.append(current_2.value)
            current_2 = current_2.next

    return result

def intersection(llist_1, llist_2):
    temp=set()
    current = llist_1.head

    while current:
        temp.add(current.value)
        current = current.next

    current = llist_2.head
    result = LinkedList()
    temp_val = set()
    while current:
        if current.value in temp and current.value not in temp_val:
            result.append(current.value)
            temp_val.add(current.value)
        current=current.next

    if result.size() == 0:
        return None
    return result

# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
#3 -> 6 -> 2 -> 32 -> 4 -> 35 -> 9 -> 65 -> 1 -> 11 -> 21 ->
print (intersection(linked_list_1,linked_list_2))
#6 -> 4 -> 21 ->

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
#3 -> 1 -> 2 -> 7 -> 4 -> 8 -> 35 -> 9 -> 6 -> 11 -> 65 -> 21 -> 23 ->
print (intersection(linked_list_3,linked_list_4))
#None



linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = []
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
#6 -> 32 -> 4 -> 9 -> 6 -> 1 -> 11 -> 21 -> 1 ->
print (intersection(linked_list_1,linked_list_2))
#6 -> 4 -> 21 ->
