#!/usr/bin/env python
# coding: utf-8

# # Building a Trie in Python
# 
# Before we start let us reiterate the key components of a Trie or Prefix Tree. A trie is a tree-like data structure that stores a dynamic set of strings. Tries are commonly used to facilitate operations like predictive text or autocomplete features on mobile phones or web search.
# 
# Before we move into the autocomplete function we need to create a working trie for storing strings.  We will create two classes:
# * A `Trie` class that contains the root node (empty string)
# * A `TrieNode` class that exposes the general functionality of the Trie, like inserting a word or finding the node which represents a prefix.
# 
# Give it a try by implementing the `TrieNode` and `Trie` classes below!

# In[2]:


## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.children = {}
        self.is_end=False
    
    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char] = self.children.get(char, TrieNode())
        

        
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        cur = self.root
        #iterate every character and insert it to the current node and change the current node to new node
        for ch in word:
            cur.insert(ch)
            cur = cur.children[ch]
        cur.is_end=True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        # return root if no prefix as input
        if not prefix:
            return self.root
        # return the current node if the prefix is found during iteration
        cur = self.root
        for ch in prefix:
            if ch not in cur.children:
                return None
            cur = cur.children[ch]
        return cur
    


# # Finding Suffixes
# 
# Now that we have a functioning Trie, we need to add the ability to list suffixes to implement our autocomplete feature.  To do that, we need to implement a new function on the `TrieNode` object that will return all complete word suffixes that exist below it in the trie.  For example, if our Trie contains the words `["fun", "function", "factory"]` and we ask for suffixes from the `f` node, we would expect to receive `["un", "unction", "actory"]` back from `node.suffixes()`.
# 
# Using the code you wrote for the `TrieNode` above, try to add the suffixes function below. (Hint: recurse down the trie, collecting suffixes as you go.)

# In[3]:


class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.children = {}
        self.is_end=False
    
    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char] = self.children.get(char, TrieNode())
        
    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        data=[]
        data = self.find_suffix(suffix,data)
        return data
    
    def find_suffix(self,suffix,suffix_list):
        ## collect the suffix if is_end is set for current node
        if self.is_end:
            suffix_list.append(suffix)
        ## otherwise recursively get all the suffixes
        for ch in self.children:
            self.children[ch].find_suffix(suffix+ch,suffix_list)
                
        return suffix_list


# # Testing it all out
# 
# Run the following code to add some words to your trie and then use the interactive search box to see what your code returns.

# In[4]:


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)
    


# In[5]:


from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact
def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')
interact(f,prefix='');


# In[92]:


# input:: a
# output:: 
# nt
# nthology
# ntagonist
# ntonym


# In[ ]:


# input:: fu
# output:: 
# n
# nction


# In[ ]:


# input:: tr
# output:: 
# ie
# igger
# igonometry
# ipod


# In[ ]:


# input:: trigger
# output:: 
# 

#since trigger is coplete word

