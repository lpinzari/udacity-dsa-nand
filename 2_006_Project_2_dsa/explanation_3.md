# Huffman Encoding

The implementation of `huffman_encoding(data)` procedure depends mainly on the following functions:

- `count_char(data)`: take a string and determine the relevant frequencies of the characters.

- `huffman_tree(chars_freq)`: Build the Huffman Tree by assigning a binary code to each character in the text.

- `get_bitstring(char_binart, data)`: create the bitstring of the data input given the binary code of each character.

The compressing algorithm has shown for the tested examples a reduction of almost *50%* of its size.

## Time and Space Complexity

Assuming an encoded text string of length ***n*** and an alphabet of ***k*** symbols:

- *Time Complexity*: For every encoded symbol you have to traverse the tree in order to decode that symbol. The tree contains ***k*** nodes and, on average, it takes ***O(log k)*** node visits to decode a symbol. So the time complexity would be ***O(n·log k)***. However, in the encoding algorithm we used a sort operation at every recursive call of the function `combine(nodes, tree)`, that approximate to ***O(k∙k log k)*** and, hence, we have ***O(k<sup>2</sup>log k)***.
- *Space Complexity*: ***O(k)*** for the tree and ***O(n)*** for the decoded text.
