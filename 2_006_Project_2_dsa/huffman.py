
import sys

def count_char(text):

    """
    create an array with the count of each character in the text input. The elements in position 0,2,4,..,2K are the number of occurrences for the corresponding character in position 1,3,5,..,2K+1.

    Args:
      text(str): text

    Returns:
       chars_freq(list): <count,character> pairs
       chars_set(list): set of chararects in the text input
    """

    chars_freq = []
    chars_set = []

    for char in text:
        if char not in chars_freq:
            freq = text.count(char)
            chars_freq.append(freq)
            chars_freq.append(char)
            chars_set.append(char)

    return chars_freq, chars_set

def huffman_tree(chars_freq):
    """
    create a huffman tree from an array of <count, characters> pairs
    see count_char(text)

    Args:
       chars_freq(list): <count,character> pairs
    Returns:
       tree(list): huffman tree
    """

    ## generate the leaves (base-level) nodes for the huffman tree frequency

    nodes = []
    while len(chars_freq) > 0:
        nodes.append(chars_freq[0:2]) # grab the (fre,char) pairs
        chars_freq = chars_freq[2:]

    ## sort in ascending order
    nodes.sort()
    tree = []
    tree.append(nodes)

    ## combine base nodes (leaves) to create the huffman tree
    huff_tree = combine(nodes,tree)

    # tree needs to be inverted - the first element in the list is the root
    huff_tree.sort(reverse=True)

    return huff_tree

def combine(nodes, tree):
    """
    recursively combines base nodes to create the huffman tree and allocates either a 0 or 1 to each pair of nodes.

    Args:
       nodes(list): leaves of the huffman tree
       tree(list): huffman tree initialized with the leaves
    Returns:
       tree(list): huffman tree
    """
    pos = 0
    new_node = []

    ## get two lowest nodes
    if len(nodes) > 1:
        nodes.sort()

        ## adds in the 0,1 to the left and right nodes
        nodes[pos].append("0")
        nodes[pos+1].append("1")

        # create a new internal node by merging the left and right nodes as children and with freq equals to the sum of the two nodes' frequencies and string equals to the concatenation of the two nodes' strings
        combined_node_freq = (nodes[pos][0] + nodes[pos+1][0])
        combined_node_string = (nodes[pos][1] + nodes[pos+1][1])
        new_node.append(combined_node_freq)
        new_node.append(combined_node_string)

        # update the nodes list with the combined node and the remaining nodes
        new_nodes = []
        new_nodes.append(new_node)
        new_nodes = new_nodes + nodes[2:]
        nodes = new_nodes

        # insert the set of nodes in the tree
        tree.append(nodes)

        # process the remaining nodes
        combine(nodes, tree)

    return tree

def get_bitstring(char_binary, data):
    """
    create the bitstring of the data input given the binary code of each character
    Args:
       char_binary(list): binary code for each character
       data(str): text to be coded
    Returns:
       bitstring(str): a string representing the binary code of data
    """
    bitstring = ""

    for char in data:
        for char_code in char_binary:
            if char in char_code:
                bitstring = bitstring + char_code[1]

    return bitstring

def get_chars(nodes):
    """
    create the set of characters given the nodes in the huffman tree.
    Args:
       nodes(list): huffman tree nodes
    Returns:
       char_set(list): a set of characters
    """
    chars_set = []
    for node in nodes:
        string = node[1]
        if len(string) == 1:
            chars_set.append(string)
    return chars_set

def huffman_encoding(data):

    chars_freq, chars_set = count_char(data)
    huff_tree = huffman_tree(chars_freq)

    ## remove duplicate items in the huffman tree and creates an array nodelist with just the nodes.

    checklist = []
    for level in huff_tree:
        for node in level:
            if node not in checklist:
                checklist.append(node)
            else:
                level.remove(node)

    # builds the binary codes for each character
    char_binary = []

    if len(chars_set) == 1:
        char_code = [chars_set[0],"0"]
        char_binary.append(char_code*len(data))
    else:
        for char in chars_set:
            charCode = ""
            for node in checklist:
                if len(node) > 2 and char in node[1]:
                    charCode = charCode + node[2]
                char_code = [char, charCode]
            char_binary.append(char_code)

    return get_bitstring(char_binary,data), huff_tree

def huffman_decoding(data,tree):

    uncompressed_string = ""
    code = ""

    ## remove duplicate items in the huffman tree and creates an array nodelist with just the nodes.

    checklist = []
    for level in tree:
        for node in level:
            if node not in checklist:
                checklist.append(node)
            else:
                level.remove(node)
    chars_set = get_chars(checklist)

    # builds the binary codes for each character
    char_binary = []

    if len(chars_set) == 1:
        char_code = [chars_set[0],"0"]
        char_binary.append(char_code*len(data))
    else:
        for char in chars_set:
            charCode = ""
            for node in checklist:
                if len(node) > 2 and char in node[1]:
                    charCode = charCode + node[2]
                char_code = [char, charCode]
            char_binary.append(char_code)
    for digit in data:
        code = code + digit
        pos = 0
        for char in char_binary:
            if code == char[1]:
                uncompressed_string = uncompressed_string + char_binary[pos][0]
                code = ""
            pos += 1
    return uncompressed_string

def test_print(text):
    print ("The size of the data is: {}\n".format(sys.getsizeof(text)))
    print ("The content of the data is: {}\n".format(text))

    encoded_data, tree = huffman_encoding(text)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    print('------------------------------------')


#%% Testing
if __name__ == "__main__":


    a_great_sentence = "the bird is the word"
    a_great_sentence2 = "This is the second test of huffman algorithm"
    a_great_sentence3 = "aaa"
    a_great_sentence4 = " "

    test_print(a_great_sentence)
    test_print(a_great_sentence2)
    print("EDGE CASES:")
    test_print(a_great_sentence3)
    test_print(a_great_sentence4)
