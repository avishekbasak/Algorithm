# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler=None):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(handler)

    def insert(self, paths, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        cur = self.root
        for path in paths:
            cur.insert(path)
            cur = cur.children[path]
        cur.handler=handler

    def find(self, paths):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no matc
        cur = self.root
        for path in paths:
            if path not in cur.children:
                return None
            cur = cur.children[path]
        return cur.handler

    def get_root_handler(self):
        return self.root.handler

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler=None):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = handler

    def insert(self, path, path_handler = None):
        # Insert the node as before
        self.children[path] = self.children.get(path,RouteTrieNode(handler=path_handler))

# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, root_handler, not_found_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.root = RouteTrie(root_handler)
        self.not_found = not_found_handler

    def add_handler(self, path, path_handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        self.root.insert(self.split_path(path),path_handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        if not path or len(path)==0:
            result = None
        elif path == '/':
            result = self.root.get_root_handler()
        else:
            if path[-1] == '/':
                path = path[:-1]
            result = self.root.find(self.split_path(path))
        if not result:
            result = self.not_found
        return result

    def split_path(self, path, delimeter='/'):
        # you need to split the path into parts for
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        return path.split(delimeter)


#test cases
# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
#root handler
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
#not found handler
print(router.lookup("/home/about")) # should print 'about handler'
#about handler
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
#about handler
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one
#not found handler
print(router.lookup(None))
#not found handler
