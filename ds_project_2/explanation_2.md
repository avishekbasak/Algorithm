Folder structure can be comparable to a tree like structure where parent directory is like the root node. So i have used BFS for traversing the complete folder structure. I have created Queue class for the queue that is used in BFS. Every path that i Encounter in the queue, I check if it is a file with valid extension then i add it to the file list to be returned, else if it is a directory, i add all its contents to the queue. This process continues till i have visited all the folders and all its files.


Time Complexity:
1. I have to visit all the file items (directory+files). so to visit all files+folders, the time complexity will be O(V) where V is the total number of file items(directory+folders) under the given path.
2. For Every directory i have to add all the file items to the queue, for which the worst case time complexity will depend on the maximum number of files present in a given directory. if the max files in a folder is K then overall complexity will be O(K)
3. So overall complexity will be O(V*K) where V is total number of file items(directory+folders) and K is max number of files present in a directory

Space Complexity:
1. I will need an auxiliary space for storing all the file paths. So it will be O(V) where V is the total number of file items(directory+folders) under the given path.
2. I will also need space to store all the files that matches the criteria. Which can be equal to the total number of file items given all the file matches the croteria
3. So overall complexity will be O(V)+O(V), which will be equivalent to O(V)
