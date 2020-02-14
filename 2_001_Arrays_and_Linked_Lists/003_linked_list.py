class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        # Move to the tail (the last node)
        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)
        return

    def to_list(self):
        # TODO: Write function to turn Linked List into Python List
        out_list = []

        node = self.head
        while node:
            out_list.append(node.value)
            node = node.next

        return out_list

# Test your method here
linked_list1 = SingleLinkedList()
linked_list1.append(3)
linked_list1.append(2)
linked_list1.append(-1)
linked_list1.append(0.2)

print ("Pass" if  (linked_list1.to_list() == [3, 2, -1, 0.2]) else "Fail")

#--------- Doubly Linked List -----------#

class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        if self.head is None:
            self.head = DoubleNode(value)
            self.tail = self.head
            return

        self.tail.next = DoubleNode(value)
        self.tail.next.previous = self.tail
        self.tail = self.tail.next
        return

# Test your class here

linked_list2 = DoublyLinkedList()
linked_list2.append(1)
linked_list2.append(-2)
linked_list2.append(4)

print("Going forward through the list, should print 1, -2, 4")
node = linked_list2.head
while node:
    print(node.value)
    node = node.next

print("\nGoing backward through the list, should print 4, -2, 1")
node = linked_list2.tail
while node:
    print(node.value)
    node = node.previous
