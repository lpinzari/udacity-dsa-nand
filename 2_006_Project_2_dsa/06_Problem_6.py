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
        out_string += "NULL"
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

    # iterators to loop over the two linked lists
    iter_1 = llist_1.head
    iter_2 = llist_2.head

    llist_U = LinkedList() # union list
    values = set() # the set of values in the two Linked lists

    if iter_1 is None and iter_2 is None:
        return llist_U

    ## loop over the two linked list and add new elements to the union set

    while iter_1:
        val = iter_1.value
        values.add(val)
        iter_1 = iter_1.next

    while iter_2:
        val = iter_2.value
        values.add(val)
        iter_2 = iter_2.next

    # iterator to loop over the union list
    iter_U = llist_U.head

    for value in values:
        if iter_U is None:
            llist_U.append(value)
            iter_U = llist_U.head
        else:
            iter_U.next = Node(value)
            iter_U = iter_U.next

    iter_U.next = None
    return llist_U

def intersection(llist_1, llist_2):

    # iterators to loop over the two linked lists
    iter_1 = llist_1.head
    iter_2 = llist_2.head


    llist_I = LinkedList() # intersection list
    values_1 = set() # the set of values in the first Linked list
    values_2 = set() # the set of values in the second Linked list

    if iter_1 is None or iter_2 is None:
        return llist_I

    ## convert the two linked list to sets

    while iter_1:
        val = iter_1.value
        values_1.add(val)
        iter_1 = iter_1.next

    while iter_2:
        val = iter_2.value
        values_2.add(val)
        iter_2 = iter_2.next

    # iterator to loop over the intersection list
    iter_I = llist_I.head

    for value in values_1:
        if value in values_2:
            if iter_I is None:
                llist_I.append(value)
                iter_I = llist_I.head
            else:
                iter_I.next = Node(value)
                iter_I = iter_I.next
    if iter_I:
        iter_I.next = None

    return llist_I



# EDGE Cases
# empty lists

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

print ('l1: {}'.format(linked_list_1))
print ('l2: {}'.format(linked_list_2))
print ('l1 or l2: {}'.format(union(linked_list_1,linked_list_2)))
print ('l1 and l2: {}'.format(intersection(linked_list_1,linked_list_2)))
print ('-----------------------------')

# only a list with repeated elements
element_2 = [1,4,5,1,1,2,5]

for i in element_2:
    linked_list_2.append(i)

print ('l1: {}'.format(linked_list_1))
print ('l2: {}'.format(linked_list_2))
print ('l1 | l2: {}'.format(union(linked_list_1,linked_list_2)))
print ('l1 & l2: {}'.format(intersection(linked_list_1,linked_list_2)))
print ('-----------------------------')

# Test case 1
# two lists with repeated elements

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)
print ('l1: {}'.format(linked_list_1))
print ('l2: {}'.format(linked_list_2))
print ('l1 | l2: {}'.format(union(linked_list_1,linked_list_2)))
print ('l1 & l2: {}'.format(intersection(linked_list_1,linked_list_2)))
print ('-----------------------------')

# two lists with distinct elements

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [1,2,4,6]
element_2 = [3,5,7,8,9]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)
print ('l1: {}'.format(linked_list_1))
print ('l2: {}'.format(linked_list_2))
print ('l1 | l2: {}'.format(union(linked_list_1,linked_list_2)))
print ('l1 & l2: {}'.format(intersection(linked_list_1,linked_list_2)))
