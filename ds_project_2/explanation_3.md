I have used the following steps for coding:
1. we traversed the data for calculating relative frequencies of each character
2. we assign binary code for each character. the more frequency word is assigned smaller code whereas less frequency word is assigned longer code
3. encode the text into compressed format with 0 and 1.
4. we will traverse the tree to decode the data with every 0 traversing left and for every 1 traversing right

Time complexity:
1. for encoding:
    a. for calculating frequency: it will be O(n + m + mlogm) where n is total number of characters and m is number of unique characters. O(n) for traversing the string and create freq map and O(m) for creating the tuple (m is number of keys ,ie, number of total unique characters) and O(mlogm) for sorting the tuple
    b. for building the tree: i have to traverse the complete list of tuple, containing letter and their frequencies. and sort the modified list on the go. it will be O(m*(m-1)log(m-1)).
    because of combination step before sorting there will always 1 less entry in list. m signifies number of unique characters
    c. for trimming, i have to visit every node of tree and trim the frequency, if the tree has k nodes then it will be O(k)
    d. for assigning code i have to visit every node of the tree, so it will be O(k) where k is number of nodes
    e. for encoding i have to traverse the complete string so it will be O(n)

    here the dominant activity is the tree building, so the overall time complexity can be said as O(m*(m-1)log(m-1)).

2. for huffman_decoding:
    a. it will be O(n) where n is  the number of characters(or rather total number of binary digits) in the encoded data.

Space complexity:
Encoding:
    a. for calculating frequency: it will be O(mk+m+m) where n is total number of characters and m is number of unique characters. O(mk) for storing frequency map; k being constant space for map each entry. O(m) for keys. and O(m) again being the tuple list. since dominant is m, so overall can be O(m)
    b. for building the tree: we create tuple of tuple to depict a tree, so number of entries will still be determined by number of unique map characters. number of nodes will be approx 2m. so space complexity O(2m), m being dominant, so over all will be O(m)
    c. for trimming, i have to do recursive call, so if k is depth of tree and O(l) is the constant space it takes for each recusrive function call, it will be O(kl)
    So overall space complexity should be O(m+kl) where m is number of unique characters, k is depth of tree and O(l) is the constant space it takes for each recusrive function call
Decoding:
    O(m+n), m being space for tree and n being the length of actual string
