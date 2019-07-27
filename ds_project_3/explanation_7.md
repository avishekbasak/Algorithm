#RouteTrieNode:
To keep track of every subpath i am using a dictionary. And for every valid end path, we will be storing the corresponding Handler
The insert adds sub path to its predecessor sub Path

Time Complexity:
insert:: O(1)
Space Complexity:
insert:: O(k) where k is the space taken by children map and handler

#RouteTrie:
Insert
We keep on adding the subpath in path list to the Route Trie, with every element as child of the previous element starting from root

Time Complexity:
O(n) where n is number of subpath in path
Space Complexity:
O(n*k) where n is the number of subpath in path and k is the space taken by children map and handler

LookUp
Starting from root we keep on looking for the existence of subpath in Route trie. If exist we return handler for the path else None
Time Complexity:
O(n) where n is number of subpath in path
Space Complexity:
O(1) since we just need space for current pointer used in iteration

#Router
Split Path:
This method splits the path string, based on delimeter
Time and Space Complexity both O(1).

Add Handler:
Call RouteTrie insert method to add the path for lookup and add the handler to the end of path.
Time Complexity:
O(n) where n is number of subpath in path
Space Complexity:
O(n*k) where n is the number of subpath in path and k is the space taken by children map and handler


Lookup:
if path is only '/' return the root handler
if path ends with '/' remove the end slash from path
invoke RouteTrie find method to check the existence of handler. Return the correct handler, else return not found handler
Time Complexity:
O(n) where n is number of subpath in path
Space Complexity:
O(1) since we just need space for current pointer used in iteration
