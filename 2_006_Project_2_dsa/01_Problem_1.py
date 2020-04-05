
class DLLNode(object):
    """
    Double Linked List Node to keep the key and value of the entry
    in the cache memory.
    """
    def __init__(self, key, val):
        self.key = key
        self.value = val
        self.next = None
        self.prev = None

    def __str__(self):
        return "(%s, %s)" % (self.key, self.value)


class LRU_Cache(object):
    """
    LRUCache utilizes an internal doubly linked list
    to maintain the least-recently-used structure:
    the head stores the Node with the most recently used key,
    and the tail stores the Node with the least recently used key.
    """

    def __init__(self, capacity):
        """
        Args:
            (int) capacity: maximum capacity in cache
        """
        if capacity < 1:
            print ("ValueError: capacity > 0")

        # PUBLIC
        self.capacity = capacity
        # PRIVATE
        self._size = 0 # number of entries stored in cache
        self._nodes_map = {} # map a key to a Node
        self._head = None  # Node with the most recently used key
        self._tail = None  # Node with the least recently used key

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self._nodes_map:
            node = self._nodes_map[key]

            # update pointers only if this is not head; otherwise return
            if self.head != node:
                self._remove(node)
                self._set_head(node)

            return node.value

        return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if key in self._nodes_map:
            node = self._nodes_map[key]
            node.value = value

            # update pointers only if this is not head; otherwise return
            if self.head != node:
                self._remove(node)
                self._set_head(node)
        else:
            new_node = DLLNode(key, value)
            if self._size == self.capacity:
                del self._nodes_map[self.tail.key]
                self._remove(self.tail)
                self._size -= 1
            self._set_head(new_node)
            self._nodes_map[key] = new_node
            self._size += 1

    def print_entries(self):
        n = self.head
        print("[head = %s, tail = %s]" % (self.head, self.tail), end=" ")
        while n:
            print("%s -> " % (n), end = "")
            n = n.next
        print("NULL")

    # PRIVATE methods

    def _set_head(self, node):
        """
        put a Node in the head (most recent) position;
        can be a new node, or node that is already stored
        """

        if self._size == 0:
            self.head = node
            self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node


    def _remove(self, node):

        if self._size == 0:
            return None

        if self._size == 1:
            self.head = None
            self.tail = None
        elif self.tail == node:
            node.prev.next = None
            self.tail = node.prev
            node.prev = None
        else:
            node.prev.next = node.next
            node.next.prev = None
            node.prev = None
            node.next = None

        return node


#----------------- LRUCache initialization ----------------#
our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);

print('our_cache.set(1,1); our_cache.set(2,2); our_cache.set(3,3); our_cache.set(4,4)')

our_cache.print_entries()

# retrieve values for existing and no-existing keys in the cache
print('our_cache.get(1): {}'.format(our_cache.get(1)))  # returns 1
our_cache.print_entries()
print('our_cache.get(2): {}'.format(our_cache.get(2)))  # returns 1
our_cache.print_entries()

print('our_cache.get(9): {}'.format(our_cache.get(9)))  # returns -1



print('our_cache.set(5,5); our_cache.set(6,6)')

our_cache.set(5, 5)
# insert new key to full capacity cache
our_cache.set(6, 6)
our_cache.print_entries()

print('our_cache.get(3): {}'.format(our_cache.get(3)))  # returns -1

# overwrite an existing key
our_cache.set(2, 5);
print('our_cache.set(3,5)')

our_cache.print_entries()

# Capacity < 1
our_cache2 = LRU_Cache(-1)
