import hashlib
import datetime

class Block:

    def __init__(self, timestamp, data, previous_hash = None):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.previous_block = None
        self.hash = self._calc_hash()

    def get_hash(self):
        return self.hash

    def get_data(self):
        return self.data

    def __str__(self):
        return 'Timestamp: {} \nData: {} \nHash: {} \nPrevious hash: {}'.format(self.timestamp, self.data, self.hash, self.previous_hash)

    ## private method
    def _calc_hash(self):
        sha = hashlib.sha256()
        hash_str = str(self.timestamp).encode('utf-8')
        hash_str += str(self.data).encode('utf-8')
        hash_str += str(self.previous_hash).encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

class BlockChain:

    def __init__(self):
        self.tail = None
        self.size = 0

    def append(self, value):
        """ Append a value to the end of the BlockChain. """

        if type(value) is not str:
            print("TypeError: argument must be a string")
            return

        if len(value) == 0:
            print("ValueError: argument string cannot be empty")
            return


        timestamp = datetime.datetime.utcnow()

        if self.tail is None:
            self.tail = Block(timestamp, value)
        else:
            last_block = self.tail
            previous_hash = last_block.get_hash()
            new_block = Block(timestamp, value, previous_hash)
            new_block.previous_block = last_block
            self.tail = new_block

        self.size += 1
        return

    def get_size(self):
        return self.size

    def to_list(self):
        # function to turn a BlockChain into a Python list
        chain_list = []

        block = self.tail
        while block:
            chain_list.append(block)
            block = block.previous_block

        return chain_list

    def print_chain(self):
        n = self.tail
        i = self.get_size() - 1
        while n:
            print('Block: {}'.format(str(i)))
            print("%s" % (n))
            n = n.previous_block
            i -= 1
            print("\n")

## for testing
def print_items(list):
    for item in list:
        print("[%s , %s]" % (item.timestamp,item.data))
    return

block_chain = BlockChain()

## empty BlockChain:
print("\t block_chain = BlockChain()")
print('size: {}'.format(block_chain.get_size()))
print_items(block_chain.to_list())
block_chain.print_chain()

print("**********************************")
## one item
block_chain.append("Data Structures & Algorithms")
print("\t block_chain.append(\"Data Structures & Algorithms \")")
print('size: {}'.format(block_chain.get_size()))
print_items(block_chain.to_list())
print("\n")
block_chain.print_chain()

print("**********************************")
# two items
block_chain.append("Programming for Data Science")
print("\t block_chain.append(\"Programming for Data Science \")")
print('size: {}'.format(block_chain.get_size()))
print_items(block_chain.to_list())
print("\n")
block_chain.print_chain()

print("**********************************")
# TypeError
print("\t block_chain.append(2)")
block_chain.append(2)
print("**********************************")
# ValueError
print("\t block_chain.append(\"\")")
block_chain.append("")
