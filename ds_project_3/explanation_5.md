In this problem, I have to implement a Trie.
TrieNode has insert & suffixes methods.
Trie contains the root node and insert/find functions
For insert it each character is added as a child of previous character and for the node where the word ends a boolean is set to indicate it is a final word.

Find works in a similar manner like insert but instead of adding it checks if every character is a child of its previous character. for the first character it is check if it exists in the root of the Trie class.

For finding suffix, we are using recursion, where we keep on visiting all its child node till we reach the end of tree; and whenever we reach a child with end marker boolean is set as True we add it to the list of suffix for return.

Time Complexity:
Insert a character O(1).
Inserting a complete word will be O(n*1) = O(n) where n is number of character in word.

Find a word: is also O(n) where n is number of character in word

Find Suffix: O(m^n) where m is maximum number of elements one level can have & n is the number of levels.

Space Complexity:
Insert a character will be O(k), where k is the space taken by children map and boolean end marker

Insert a word: O(n*k) where n is the number of characters in a word and k is the space taken by children map and boolean end marker
Find a prefix: O(1) since we just need space for current pointer used in iteration

Find Suffix: O(m^n) where m is maximum number of elements one level can have & n is the number of levels, to store all the suffixes.
