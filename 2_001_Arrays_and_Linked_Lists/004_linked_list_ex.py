# Implement a linked list class. Your class should be able to:
#
# Append data to the tail of the list and prepend to the head
# Search the linked list for a value and return the node
# Remove a node
# Pop, which means to return the first node's value and delete the node from the list
# Insert data at some position in the list
# Return the size (length) of the linked list

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, value):
        """ Prepend a node to the beginning of the list """

        if self.head is None:
            self.head = Node(value)
            return

        new_head = Node(value)
        new_head.next = self.head
        self.head = new_head

    def append(self, value):
            """ Append a node to the end of the list """
            # Here I'm not keeping track of the tail. It's possible to store the tail
            # as well as the head, which makes appending like this an O(1) operation.
            # Otherwise, it's an O(N) operation as you have to iterate through the
            # entire list to add a new tail.

            if self.head is None:
                self.head = Node(value)
                return

            node = self.head
            while node.next:
                node = node.next

            node.next = Node(value)

    def search(self, value):
            """ Search the linked list for a node with the requested value and return the node. """
            if self.head is None:
                return None

            node = self.head
            while node:
                if node.value == value:
                    return node
                node = node.next

            raise ValueError("Value not found in the list.")

    def remove(self, value):
            """ Delete the first node with the desired data. """
            if self.head is None:
                return

            if self.head.value == value:
                self.head = self.head.next
                return

            node = self.head
            while node.next:
                if node.next.value == value:
                    node.next = node.next.next
                    return
                node = node.next

            raise ValueError("Value not found in the list.")

    def pop(self):
            """ Return the first node's value and remove it from the list. """
            if self.head is None:
                return None

            node = self.head
            self.head = self.head.next

            return node.value

    def insert(self, value, pos):
            """ Insert value at pos position in the list. If pos is larger than the
                length of the list, append to the end of the list. """

            node = self.head

            if pos <= 0 or node is None:
                self.prepend(value)
                return

            index = 0

            while node.next:
                if (pos - 1) == index:
                    new_node = Node(value)
                    new_node.next = node.next
                    node.next = new_node
                    return

                index += 1
                node = node.next

            self.append(value)

    def size(self):
        """ Return the size or length of the linked list. """
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out

## Test your implementation here

# Test prepend
linked_list = LinkedList()
linked_list.prepend(1)
assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
linked_list.append(3)
linked_list.prepend(2)
assert linked_list.to_list() == [2, 1, 3], f"list contents: {linked_list.to_list()}"

# Test append
linked_list = LinkedList()
linked_list.append(1)
assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
linked_list.append(3)
assert linked_list.to_list() == [1, 3], f"list contents: {linked_list.to_list()}"

# Test search
linked_list.prepend(2)
linked_list.prepend(1)
linked_list.append(4)
linked_list.append(3)
assert linked_list.search(1).value == 1, f"list contents: {linked_list.to_list()}"
assert linked_list.search(4).value == 4, f"list contents: {linked_list.to_list()}"

# Test remove
linked_list.remove(1)
assert linked_list.to_list() == [2, 1, 3, 4, 3], f"list contents: {linked_list.to_list()}"
linked_list.remove(3)
assert linked_list.to_list() == [2, 1, 4, 3], f"list contents: {linked_list.to_list()}"
linked_list.remove(3)
assert linked_list.to_list() == [2, 1, 4], f"list contents: {linked_list.to_list()}"

# Test pop
value = linked_list.pop()
assert value == 2, f"list contents: {linked_list.to_list()}"
assert linked_list.head.value == 1, f"list contents: {linked_list.to_list()}"

# Test insert
linked_list.insert(5, 0)
assert linked_list.to_list() == [5, 1, 4], f"list contents: {linked_list.to_list()}"
linked_list.insert(2, 1)
assert linked_list.to_list() == [5, 2, 1, 4], f"list contents: {linked_list.to_list()}"
linked_list.insert(3, 6)
assert linked_list.to_list() == [5, 2, 1, 4, 3], f"list contents: {linked_list.to_list()}"

# Test size
assert linked_list.size() == 5, f"list contents: {linked_list.to_list()}"
