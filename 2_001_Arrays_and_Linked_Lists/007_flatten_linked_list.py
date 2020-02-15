# Flattening a nested linked list
# Suppose you have a linked list where the value of each node is a sorted linked list (i.e., it is a nested list). Your task is to flatten this nested list—that is, to combine all nested lists into a single (sorted) linked list.
#
# First, we'll need some code for generating nodes and a linked list:

# Use this class as the nodes in your linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)

class LinkedList:
    def __init__(self, head):
        self.head = head

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = Node(value)

# solve the problem by implementing the flatten method.
#
# Hint: If you first create a merge method that merges two linked lists into a sorted linked list, then there is an elegant recursive solution.

# First, let's implement a merge function that takes in two linked lists and returns one sorted linked list. Note, this implementation expects both linked lists to be sorted.

def merge(list1, list2):
    merged = LinkedList(None)
    if list1 is None:
        return list2
    if list2 is None:
        return list1
    list1_elt = list1.head
    list2_elt = list2.head
    while list1_elt is not None or list2_elt is not None:
        if list1_elt is None:
            merged.append(list2_elt)
            list2_elt = list2_elt.next
        elif list2_elt is None:
            merged.append(list1_elt)
            list1_elt = list1_elt.next
        elif list1_elt.value <= list2_elt.value:
            merged.append(list1_elt)
            list1_elt = list1_elt.next
        else:
            merged.append(list2_elt)
            list2_elt = list2_elt.next
    return merged

# Let's make sure merge works how we expect:

linked_list = LinkedList(Node(1))
linked_list.append(3)
linked_list.append(5)

second_linked_list = LinkedList(Node(2))
second_linked_list.append(4)

merged = merge(linked_list, second_linked_list)
node = merged.head
while node is not None:
    #This will print 1 2 3 4 5
    print(node.value)
    node = node.next

# Lets make sure it works with a None list
merged = merge(None, linked_list)
node = merged.head
while node is not None:
    #This will print 1 3 5
    print(node.value)
    node = node.next


# Now let's implement flatten recursively using merge.

class NestedLinkedList(LinkedList):
    def flatten(self):
        return self._flatten(self.head)

    def _flatten(self, node):
        if node.next is None:
            return merge(node.value, None)
        return merge(node.value, self._flatten(node.next))


nested_linked_list = NestedLinkedList(Node(linked_list))
nested_linked_list.append(second_linked_list)
flattened = nested_linked_list.flatten()

node = flattened.head
while node is not None:
    #This will print 1 2 3 4 5
    print(node.value)
    node = node.next
