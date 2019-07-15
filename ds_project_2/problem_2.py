import os
from collections import deque

# Folder structure can be comparable to a tree like structure where parent directory is like the root node
# So i have used BFS for traversing the complete folder structure
# I have created Queue class for the queue that is used in BFS. Every path that i Encounter in the queue, I check if it is a file with valid extension
# then i add it to the file list to be returned, else if it is a directory, i add all its contents to the queue. This process continues till i have visited
# all the folders and all its files.
class Queue():
    def __init__(self):
        self.q = deque()

    def enq(self,value):
        self.q.appendleft(value)

    def deq(self):
        if len(self.q) > 0:
            return self.q.pop()
        else:
            return None

    def __len__(self):
        return len(self.q)



def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    # files to be returned
    file_list = []

    #return none if input is invalid
    if path is None or suffix is None or len (suffix) == 0 or len(path) == 0:
        return None
    #define the queue
    q = Queue()
    # add the incoming path to queue
    q.enq(path)
    #iterate till the queue is empty
    while len(q) > 0:
        #get the first value in queue
        val = q.deq()
        #check if the popped path is a file that ends with the suffix, if yes then add it to the list to return
        if valid_file(suffix,val):
            file_list.append(val)
        # if the path is a directory add all the items in the queue
        else:
            add_file_to_q(val,q)
    if len(file_list) == 0:
        return None
    return file_list


def valid_file(suffix,path):
    '''
    Method checks if it is a valid file that needs to be retrieved
    '''
    if os.path.isfile(path):
        ext = os.path.splitext(path)[-1].lower()
        if ext == suffix:
            return True
    return False

def add_file_to_q(path,q):
    '''
    Method retrieves all the items in the given path and add it to the Queue
    '''
    if os.path.isdir(path):
        listDir = os.listdir(path)
        if len(listDir) > 0:
            for fp in listDir:
                q.enq(path+"/"+fp)

print(find_files('.c','/Users/avishekbasak/algo_udacity/testdir'))
#['/Users/avishekbasak/algo_udacity/testdir/t1.c',
#'/Users/avishekbasak/algo_udacity/testdir/subdir5/a.c',
#'/Users/avishekbasak/algo_udacity/testdir/subdir1/a.c',
#'/Users/avishekbasak/algo_udacity/testdir/subdir3/subsubdir1/b.c']

print(find_files('','/Users/avishekbasak/algo_udacity/testdir'))
# None
print(find_files('.c',''))
# None
print(find_files(None,'/Users/avishekbasak/algo_udacity/testdir'))
# None
print(find_files('.c',None))
# None
print(find_files('.py','/Users/avishekbasak/algo_udacity/testdir'))
# None
print(find_files('.h','/Users/avishekbasak/algo_udacity/testdir'))
#['/Users/avishekbasak/algo_udacity/testdir/t1.h',
#'/Users/avishekbasak/algo_udacity/testdir/subdir5/a.h',
#'/Users/avishekbasak/algo_udacity/testdir/subdir1/a.h',
#'/Users/avishekbasak/algo_udacity/testdir/subdir3/subsubdir1/b.h']
print(find_files('.h','/Users/avishekbasak/algo_udacity'))
#['/Users/avishekbasak/algo_udacity/testdir/t1.h',
#'/Users/avishekbasak/algo_udacity/testdir/subdir5/a.h',
#'/Users/avishekbasak/algo_udacity/testdir/subdir1/a.h',
#'/Users/avishekbasak/algo_udacity/testdir/subdir3/subsubdir1/b.h']

print(find_files('.h','/XUsers/avionic/'))
# None
