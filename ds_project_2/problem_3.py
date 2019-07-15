import sys

def huffman_encoding(data):
    """
    this method encodes the data and return the encoded data and Tree
    """

    if data is None:
        return 0,None

    if len(data)==0:
        return 1,None

    # calculate the frequency and construct tuples of freq to
    tuples = calculate_freq(data)
    #Build and sort a list of tuples from lowest to highest frequencies
    #Build the Huffman Tree by assigning a binary code to each letter, using shorter codes for the more frequent letters
    #print(tuples)
    tree = buildTree(tuples)
    #trim the tree to be sorter
    tree = trimTree(tree)
    #print(tree)
    codes = {}
    #get binary code for each character
    assignCodes(tree,codes)
    #encode the data
    #print(codes)
    output = ""
    for ch in data :
        output += codes[ch]
    return output, tree

def huffman_decoding(data,tree):
    '''
    this method decodes the binary data to proper string
    '''
    output = ""
    temp = tree
    if data == 0 and tree is None:
        return None
    if data == 1 and tree is None:
        return ''
    for ch in data :
        #if the character is 0 go towards left else go towards right of the tree
        if ch == '0' :
            temp = temp[0]
        else:
             temp = temp[1]
        #if p is a simmple string or a leaf node, then add the string to the output
        if isinstance(temp, str) :
            output += temp
            #reset temp to start from the root
            temp = tree
    return output

def calculate_freq(data):
    '''
    this method calculates frequency of each word and creates a list of tuple consisting of the letter and its total count in a sorted way
    '''
    freq = {}
    keys = set()
    #calculates count of each character
    for char in data :
        freq[char] = freq.get(char,0) + 1
        keys.add(char)
    #create the tuple from freq
    char_freq_tuples = []
    for ch in keys:
        char_freq_tuples.append((ch,freq[ch]))
    #sort the letters based on freq
    char_freq_tuples.sort(key=lambda t: t[1])
    return char_freq_tuples

def buildTree(tuples) :
    '''
    this method build the tree from the tuple frequency
    '''
    #keep iterating till the list contains one single tuple
    while len(tuples) > 1 :
        #get minimum two freq from the sorted list
        minimum_two = tuple(tuples[0:2])
        rest  = tuples[2:]
        #commbined the frequencies and add them back to the list
        combFreq = minimum_two[0][1] + minimum_two[1][1]
        tuples   = [(minimum_two,combFreq)] + rest
        #sort the frequency
        tuples.sort(key=lambda t: t[1])
    return tuples[0]


def trimTree (tree) :
    '''
     this method trims the freq counters off, leaving only the letters
    '''
    temp = tree[0]
    #if p is a simple string / a leaf node return the string else trim it again
    if isinstance(temp, str) :
        return temp
    else :
        return (trimTree(temp[0]), trimTree(temp[1])) # trim left then right and recombine


def assignCodes (node, codes, pat='') :
    '''
    this method assigns code to each character
    '''
    #if node is a simple string / a leaf node add set the code for the character
    if isinstance(node, str)  :
        codes[node] = pat
    else:
        #add 0 for each left branch point
        assignCodes(node[0], codes, pat+"0")
        #add 1 for each right branch point
        assignCodes(node[1], codes, pat+"1")

if __name__ == "__main__":

    #test 1
    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    #The size of the data is: 69
    print ("The content of the data is: {}\n".format(a_great_sentence))
    #The content of the data is: The bird is the word

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    #The size of the encoded data is: 36
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    #The content of the encoded data is: 1110111010111011001000010001100001111110111101101011101100011100010001

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    #The size of the decoded data is: 69
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    #The content of the encoded data is: The bird is the word

    #test 2

    a_great_sentence = None

    print ("The content of the data is: {}\n".format(a_great_sentence))
    #The content of the data is: None
    encoded_data, tree = huffman_encoding(a_great_sentence)
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    #The content of the encoded data is: 0

    decoded_data = huffman_decoding(encoded_data, tree)
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    #The content of the encoded data is: None

    #test 3

    a_great_sentence = ''

    print ("The content of the data is: {}\n".format(a_great_sentence))
    #The content of the data is:
    encoded_data, tree = huffman_encoding(a_great_sentence)
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    #The content of the encoded data is: 1

    decoded_data = huffman_decoding(encoded_data, tree)
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    #The content of the encoded data is:

    #test 4

    a_great_sentence = 'adihkjhada&&^%!(*098)'

    print ("The content of the data is: {}\n".format(a_great_sentence))
    #The content of the data is: adihkjhada&&^%!(*098)
    encoded_data, tree = huffman_encoding(a_great_sentence)
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    #The content of the encoded data is: 10100111000000111101101000010100110110010011111011101101110011011111010100010111001

    decoded_data = huffman_decoding(encoded_data, tree)
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    #The content of the encoded data is: adihkjhada&&^%!(*098)
