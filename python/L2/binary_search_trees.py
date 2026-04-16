# As a senior backend developer you are tasked with developing a fast in memory data structure to manage profile information (username,name,email) for 100 million users and it should allow the following operations to be performed efficiently :
# 1. Insert the profile information of a new user 
# 2. find the profile information of a user, given their username
# 3. Update the profile information of a user, given their username
# 4. List all the users of the platform, sorted by username 

# assume that usernames are unique 

# Step 1 :- 

# to put the problem simply it means that we need to create a data structure which can store 100 million records and perform insertion, search, update and list operations efficiently 

# Inputs :- main input is user profile which contains username, name and email of a user 
# We will use a class to represent the information for the user 

class User():
    """
    Represents a user profile
    """

    def __init__(self,username,name,email): # constructor 
        self.username = username
        self.name = name
        self.email = email
         

    def introduce_yourself(self):
        print(f"Hi {self.username}, I'm {self.name}, Contact me at {self.email}")

user1 = User('david', 'jane doe', 'janedoe@gmail.com')
user1.introduce_yourself() # calling introduce_yourself method on user object called user1
print()

def __repr__(self): # official object representation
    return(f"User(username = '{self.username}', name = '{self.name}', email = '{self.email}')")

def __str__(self): # readable string version 
    return self.__repr__()
        
User.__repr__ = __repr__
User.__str__ = __str__
    
print(user1)
print()

# Output

class UserDatabase:
    def insert(self,user):
        pass

    def find(self,username):
        pass

    def update(self,user):
        pass

    def list_all(self):
        pass

# Step 2 :- 

# some input examples 

aakash = User('aakash', 'Aakash Rai', 'aakash@example.com')
biraj = User('biraj', 'Biraj Das', 'biraj@example.com')
hema = User('hema', 'Hema Jain', 'heman@example.com')
jadhesh = User('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com')
siddhant = User('siddhant', 'Siddhant Sinha', 'siddhant@example.com')
sonaksh = User('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com')
viru = User('viru', 'Viru Goel', 'viru@example.com')

print(hema)
print()

users = [aakash,biraj,hema,jadhesh,siddhant,sonaksh,viru]

print(biraj.username, biraj.name, biraj.email)
print()

# print(users)
print()



# Step 3 :- 

# to put the solution simply : we store the User objects in list sorted by usernames 
# here is how we can implement different functions :- 

# insert :- Loop through the list and add the user at a position that keeps the list sorted
# find :- Loop through the list and find the user object with the username matching the query 
# update :- Loop through the list, find the user object matching the query and update the details
# list_all :- return the list of user objects 

# usernames can be compared using <, >, == operators

print('biraj' < 'viru') # b comes before v so this is True
print()

# Step 4 :- 

# implementation of the solution goes like this 

class UserDatabase:
    def __init__(self):
        self.users = [] # whenever a new database is made it always start with an empty list in an example below when we do database = User_database this line will convert into database.users = []
    
    def insert(self,user): # will take self(the database object) and user(the new user object to insert)
        i = 0 # counter to start from index 0 
        while i < len(self.users): # if the list have 5 users the counting should be from 0-4 and when it reaches 5 this condition becomes false and we exit the loop 
            if self.users[i].username > user.username: # to check if the current which is [i] , user's username is greater than the new user's username we are inserting 
                break # stop the loop if above condition is true, it means we have found where new user belongs
            i += 1 # else increment the counter so that we can move to next index 
        self.users.insert(i,user) # what happening here is that we are using a list method called insert() with syntax list.insert(index,element) and what it essentially mean is that put this element at this index and shift everything to right  

    def find (self,username): # searching using username as the input
        for user in self.users: # loop through every user in list one by one 
            if user.username == username: # if user's username matches the one we are searching 
                return user
            
    def update(self,user): # to update an existing user's detail, this method receives a new user object containing updated information as an argument 
        target = self.find(user.username) # find the existing user in the database whose username matches the new username 
        target.name, target.email = user.name, user.email # here we are doing something called python multiple assignment where we updating the existing values of the user by assigning them new values (old values = new values) and here we are just changing the name and email because username is our unique key here and the sorted order depends on it 

    def list_all(self):
        return self.users # returning the list 
    
database = UserDatabase() # instance object of UserDatabase class or to put it simply its a user database


database.insert(aakash)
database.insert(biraj)
database.insert(viru)

user = database.find('biraj')
print(user)
print()

database.update(User(username='biraj', name='Biraj D', email='Biraj@gmail.com'))

user = database.find('biraj')
print(user)
print()

print(database.list_all())
print()

database.insert(hema)


print(database.list_all())
print()


# Step 5 :- 

# analyze algos complexity and inefficiencies 

# insert :- O(N)
# find :- O(N)
# update :- O(N)
# list_all :- O(1)

# insert,find and update takes O(N) linear time complexity because in worst case scenario the algo need to check each element in the list to perform these operations and with each inc in length of list the steps to perform also increases linearly and list_all have O(1) constant time complexity because no matter how big the list becomes list_all just have to return the whole list one time 

# The overall storage operation is O(N) space because with each additional user the memory required to store them also increases but the space complexity of the operations remain O(1) auxiliary space (extra temporary memory an algo uses while running) which means the algo uses only a fixed amount of extra memory no matter how large the input becomes 

# import time

# start_wall = time.perf_counter() # performance counter for measuring wall time i.e real world time elapsed during the process
# start_cpu = time.process_time() # process time for cpu time i.e time taken by cpu to perform operation

# for i in range(100000000):
#     j = i * i

# end_wall = time.perf_counter()
# end_cpu = time.process_time()

# print(f"CPU time: {end_cpu - start_cpu:.2f} seconds")
# print(f"Wall time: {end_wall - start_wall:.2f} seconds")
# print()


# this loop takes some time to process and if same thing happens when we are trying to fetch user data it will lead to sub optimal user experience which will most probably turn into user stopping to use the platform using this kind of fetching and other operations and if multiple users are trying to access user profile at same time with this kind of delay will lead to increase cost of cloud infrastructure to the company 

# As our question demands as a senior backend engineer, you must come up with a more efficient data structure! Choosing the right data structure for the requirements at hand is an important skill. It's apparent that a sorted list of users might not be the best data structure to organize profile information for millions of users 




# Step 6 :- 

# the right technique to overcome our previous issues we can limit the iterations required for common operations like insert, find and update by organizing our data in a binary tree 

# Its called a tree because the data structure we are talking is like a inverted tree with trunk on the upper side and branches spreading downward 

# The word binary here indicates that each node in a tree can have at most 2 children(left or right)

# Nodes can have 0,1 or 2 children. Nodes that do not have a children are sometimes called leaf nodes (usually the last nodes that dont have any children) 

# the single node at the top is called the root node and its generally where operations like insertion and search begins.

# For our use case we need the binary tree to have some more additional properties
  
# 1. Keys and values :- Each node of the tree stores a key (the username) and a value (a user object). A binary tree where nodes have both a key and a value is often referred to as a map or tree map because it maps keys to values 

# 2. Binary search tree :- when the left subtree of any node have keys that are alphabetically smaller than the main node and the right subtree have the keys that are alphabetically larger than the main node the tree is called a binary search tree and this property makes it easier to locate a specific key by traversing a single path down from the root node 

# 3. Balanced tree :- when a tree dont skew heavily on one side that means the left and right subtrees of any node should not differ in height/depth by more than one level to put it simply the tree is equal on each side thats when its called a balanced tree


# Height of a binary tree 

tree_repr0 = """

      A        ← Level 0
     / \
    B   C      ← Level 1
   / \  / \ 
   D  E F  G   ← Level 2

"""

# The number of levels you go down is the height and in above example height = 3 levels (0,1,2) and this is calculated like this because each node have a left and right child and we start from the root (level 0 - 1 node) , (level 1 - 2 nodes), (level 2 - 4 nodes) and they always increase in power of 2

# Total nodes at height 3 are 1 + 2 + 4 = 7 nodes, and at height 5 the total nodes become 1 + 2 + 4 + 8 + 16 = 31 nodes and at height 10 the total nodes become 1023 so we can see that if a tree grows this way it spreads wide very fastly even if the height increase is not that fast 

# Now instead of asking if height is (k) then how many nodes it have, we can ask if i have N nodes then how tall is the tree 

# The formula used to calculate total nodes of a perfect binary tree with height (k) starting the counting from level 0 is N = 2^k - 1 so if someone asks how many nodes in a binary tree with height 4 we can calculate like N = 2^4 (2*2*2*2=16) - 1 = 16-1 = 15 so a binary tree with height 4 have total 15 nodes 

# And the formula used to calculate the height of the binary tree if we have the nodes (N) is first we take our previous formula N = 2^k - 1 and add +1 to both sides of = which becomes N + 1 = 2^k - 1 + 1 so after 1st simplification it becomes N + 1 = 2^k and now we take log2(because nodes increases always in power of 2) of N + 1 and simplify the equation further which becomes k = log2(N+1) and if we try to solve the question where if someone asks what is the height of the binary tree that have 15 nodes we can calculate like k = log2(15+1=16) so log2(16) means how many times we have to multiply 2 to get 16 and that calculates to 2*2*2*2 = 16 so 4 times. So the height of a tree that have 15 nodes is 4.

# The important realization is that in a balanced tree we dont check all nodes like a list instead we traverse a single path from root to leaf and the length of this path is equal to the height of the tree and since we proved that the nodes increases exponentially and height increases logarithmically with N = 2^k -1 & k = log2(N+1) respectively we can deduce from it that height is equivalent to log(N) and to put it more simply it just means if the number of nodes becomes very big the number of levels dont increase to its proportion and a tree can store many nodes without becoming too tall and due to this equivalence all operations like insert, find, update take O(logN) logarithmic time to complete (steps = logN). More will be discussed about this later 


# Implement a binary tree 

# we will be implementing a simple binary tree without any additional properties and containing numbers as keys within nodes 

class TreeNode:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

node0 = TreeNode(3)
node1 = TreeNode(4)
node2 = TreeNode(5)

print(node1.key)
print()

# we can connect the nodes by setting the .left and .right properties of the root node by doing :-

node0.left = node1
node0.right = node2

# now this tree looks like 

tree_repr1 = """
    3
   / \
  4   5
"""

# we can make a variable called tree which points to root node and use it to access all nodes within the tree :-

tree = node0
print(tree.key)
print()

print(tree.left.key)
print()

print(tree.right.key)
print()


# Going forward we will use term tree to refer to the root node and term node can refer to any node in a tree not necessarily the root


# Create the following binary tree using the class TreeNode :- 

tree_repr2 = """
        2
       / \
      3   5
     /   / \
    1   3   7
         \  / \
          4 6  8
"""

# Here instead of connecting the nodes one by one we will write a helper function which will convert a tuple which we are using to simplify the nodes structure data to a binary tree 

# the tuple we are using have the structure like this (left_subtree, key, right_subtree) where ((left_subtree)) and ((right_subtree)) are tuples in themselves so that makes the whole expression as ((left_subtree), key, (right_subtree)) and this is a generalized expression i wrote the inner tuple of left and right subtrees will expand within themselves depending on number of nodes and will be shown below with examples 

# here is a tuple representing the tree above 

tree_tuple = ((1,3,None), 2, ((None,3,4), 5, (6,7,8)))

# now we will write the function 

# what this function will be doing is that its saying give me the tree data in tuple form and i will convert it into actual connected TreeNode objects 

def parse_tuple(data): # Defining a parameter automatically creates a variable that stores whatever argument is passed during the function call.In our case its data which will be the tuple that we will pass as a argument when calling the function
    if isinstance(data,tuple) and len(data) == 3 : # This condition here is to check if the data we are giving the function represents a subclass in tuple form by doing if isinstance(data,tuple) which means we are using isinstance function which have the syntax isinstance(object,classinfo) which lets us check if the object is an instance of a class or subclass and we are also checking the len of data is == 3 because our basic structure of a tuple is (left_subtree,key,right_subtree)
        node = TreeNode(data[1]) # here we are creating the central node of the tree by calling TreeNode with data at index 1 which will always be the key and this applies to the 1st root as well as the root of the subtree 
        node.left = parse_tuple(data[0]) # Recursive case
        node.right = parse_tuple(data[2]) # Recursive case 
    elif data is None: # Base case
        node = None
    else: # Base case 
        node = TreeNode(data)
    return node



# I wrote a detailed explanation of what the data flow looks like for the above written function on pen and paper so i wont spend more time writing it here for now ill move forward and write it as docs here when i come back here to revise 


tree2 = parse_tuple(tree_tuple)
print(tree2.key) # main root node (2)
print(tree2.left.key,tree2.right.key) # next nodes in tree (3,5)
print(tree2.left.left.key, tree2.left.right, tree2.right.left.key, tree2.right.right.key) # next nodes (1,None,3,7)
print(tree2.right.left.right.key, tree2.right.right.left.key, tree2.right.right.right.key) # nodes of nodes (3,7) :- (4,6,8)
print()


# Now we will write a function tree_to_tuple which will convert a binary tree into a tuple representing the same tree so this function is the reverse of what we did above.

def tree_to_tuple(node):
        if node is None:
            return None
        if node.left is None and node.right is None:
            return node.key
        return TreeNode.to_tuple(node.left),  node.key, TreeNode.to_tuple(node.right)



# We will also write a helper function to display all the keys in a tree like structure for easier visualization 

def display_keys(node, space = '\t', level = 0): # node = current node, space = '\t to put a tab space, level = 0 :- depth of current node (starts from 0 at root)

    # if node is empty

    if node is None: # we do this to represent None in the tree when there is no child in the connecting node we depict it by '∅'. To put it simply when recursion hit the missing child we depict it by '∅'
        print(space*level + '∅')
        return 
    
    # if node is leaf

    if node.left is None and node.right is None: # this code block means is that if the node that we are currently on is a leaf having no left or right child
        print(space*level + str(node.key)) # print its value in the correct position 
        return # then stop going deeper and return 
    
    # if nodes have children

    display_keys(node.right, space, level + 1)
    print(space*level + str(node.key))
    display_keys(node.left,space,level + 1)

display_keys(tree2)
print('\n')
print('\n')

tree_tuple2 = ((2),1,(3))
tree3 = parse_tuple(tree_tuple2)
display_keys(tree3)
print('\n')
print('\n')

# For this the Call-1 happens in display_keys as display_keys(node=1,level=0)
 
# Then it checks the if condition which turns out to be False as node is not None

# Then it checks our 2nd if condition which again turns out to be False because of node do have a left and right child so this condition also gets skipped
 
# so the function moves to display_keys(node.right,space,level+1) and here the current value of node.right = 3, space = '\t', level = 0 so our line becomes display_keys(3,'\t',0+1=1)

# At this point Call 1 is paused at display_keys(node.right,space,level+1) and will only move further in its own block after this is solved.

# Now Call-2 happens display_keys(node = 3, level = 1)

# so we check our 1st if condition again which turns out to be False
 
# Then we check our 2nd if condition which turns out to be True because node 3 dont have a left or right child
 
# so now we execute the next line print(space*level + str(node.key)) which becomes print('\t' * 1 + '3') = print('\t3') so output becomes     3 . and then it gets returned upwards because this Call 2 is finished now.
 
# now we come back to Call 1, we have solved and printed right subtree which is (3)

# now we move to this line in Call 1 which is print(space*level + str(node.key)) and here the values are space='\t' * level=0 + node.key = 1 so that makes it str(1) and we print 1 

# Then we move to next line in Call 1 which is display_keys(node.left, space, level+1) which when substituted the values in becomes node.left = 2, space = '\t', level = 0 and that looks display_keys(2, '\t', 1)

# Now we enter Call 3 

# display_keys(node=2,level=1)

# we check our 1st if condition which turns out as False then we move to 2nd if condition which turns out to be true 

# so we do print(space*level + str(node.key)) which becomes print('\t' * 1 + '2') and prints     2 . and returns the node 

# and we are done with the function 


# Traversing the binary tree 

# Traversal in a binary tree means moving through the tree in a specific order and visiting every node exactly one time.

# Visiting a node simply means performing some action on it such as printing its value, storing it in a list, counting it, or using it in some logic.

# Different traversal orders visit the same nodes in different sequences, which is why traversal is important.


# Depth First Traversal (DFS) is a way of traversing a tree in which we go as deep as possible along one branch before backtracking and exploring other branches.
# It explores nodes level by level in depth rather than visiting all nodes at the same level.
# Inorder, Preorder, and Postorder traversals are all types of depth first traversal.

# INORDER TRAVERSAL 

# Inorder traversal is a depth first traversal technique in which we first visit the left subtree, then the current node, and finally the right subtree.
# In a Binary Search Tree (BST), inorder traversal visits the nodes in sorted order.
# Rule :- Left -> Node -> Right

# PREORDER TRAVERSAL

# Preorder traversal is a depth first traversal technique in which we first visit the current node, then the left subtree, and finally the right subtree.
# This traversal is useful when we want to process the root before its children.
# Rule :- Node -> Left -> Right

# POSTORDER TRAVERSAL 

# Postorder traversal is a depth first traversal technique in which we first visit the left subtree, then the right subtree, and finally the current node.
# This traversal is useful when we want to process child nodes before their parent.
# Rule :- Left -> Right -> Node


# now we will write code for each 

def traversal_inorder(node): # This function takes one node and returns the inorder traversal of the tree rooted at that node
    if node is None: # if no node return an empty list
        return []
    return (traversal_inorder(node.left) + [node.key] + traversal_inorder(node.right)) # to put it simply this means inorder traversal of this tree is inorder traversal of left subtree then current node then inorder traversal of right subtree. Give me inorder traversal list of left subtree + the current node + inorder traversal list of right subtree

print(traversal_inorder(tree3))
print()

# when we call this function the node = 1 and since the node is not None we execute and return the 2nd return condition which becomes traversal_inorder(2) + [1] + traversal_inorder(3) # this is call 1

# But the code cant return it yet because the traversal_inorder(2) and traversal_inorder(3) are not yet solved 

# so call 2 happens with node = 2 and we again execute the 2nd return statement which comes out as traversal_inorder(None) + [2] + traversal_inorder(None)

# now a call which i will designate as call 2.1 happens inside call 2 to solve traversal_inorder(None) which fulfills the 1st condition where node is None and return us with an empty list [] it returns the empty list back to call 2 and it makes our line return [] + [2] 

# Then call 2.2 happens inside call 2 to solve the right side traversal_inorder(None) which returns [] upwards to call 2 and now we have return [] + [2] + [] which becomes [2] now call 2 is finished and return this upward to call 1 where traversal_inorder(2) becomes [2] and our line becomes [2] + [1] + traversal_inorder(3)

# now we solve for traversal_inorder(3) so here our call 3 starts and same call 3.1 and 3.2 happens inside it which returns empty list because there are no nodes left or right of node 3 and call 3 returns [] + [3] + [] = [3] upwards to call 1

# now call 1 return statement looks like [2] + [1] + [3] = [2,1,3] which gets returned to us 



def traversal_preorder(node):
    if node is None:
        return []
    return ([node.key] + traversal_preorder(node.left) + traversal_preorder(node.right))

print(traversal_preorder(tree3))
print()

# call 1 we call the function and our 2nd return statement becomes return ([1] + traversal_preorder(2) + traversal_preorder(3))

# now call 2 happens and we call traversal_preorder(2), it returns ([2] + [] + []) = [2] with call 2.1 and 2.2 also happening which get returned upwards to call 1, which becomes return [1] + [2] + traversal_preorder(3)

# now call 3 happens, we call traversal_preorder(3) which executes 2nd return statement and internally also execute call 3.1 and 3.2 ultimately we get [3] + [] + [] = [3] and it gets returned to call 1 which becomes [1] + [2] + [3] = [1,2,3] 


def traversal_postorder(node):
    if node is None:
        return []
    return (traversal_postorder(node.left) + traversal_postorder(node.right) + [node.key])

print(traversal_postorder(tree3))
print()

# call 1 happens by calling traversal_postorder(tree3) and it executes 2nd return statement which becomes return (traversal_postorder(2) + traversal_postorder(3) + [1])

# now call 2 happens to solve traversal_postorder(2) with internal calls 2.1 and 2.2, this call returns [] + [] + [2] = [2] to call 1 upwards and call 1 now becomes return [2] + traversal_postorder(3) + [1]

# now call 3 happens to solve traversal_postorder(3) with internal calls 3.1 and 3.2, this call returns [] + [] + [3] = [3] upwards to call 1 and now our line in call 1 becomes return [2] + [3] + [1] = [2,3,1] as the final answer


# now we will add code for getting tree height/depth and tree size (count number of nodes) too


def tree_height(node): # This function takes the node and returns the height of the tree rooted at that node
    if node is None: # base case if there is no node 
        return 0
    return 1 + max(tree_height(node.left), tree_height(node.right)) # recursive case that means the height is 1 for this node + the bigger height between left or right subtree that why we are using the max function which is used to find the largest item in an iterable data structure or largest of the 2 arguments 

print(tree_height(tree3))
print(tree_height(tree2))
print()

# for tree3 call 1 happens with node = 1 so the 2nd return condition gets executed which makes it 1 + max(tree_height(2), tree_height(3)) and this pauses here 

# now call 2 happens with calling tree_height(2) and inside it executes the 2nd return condition which makes it 1 + max(tree_height(None), tree_height(None)), now it again pauses here and call 2.1 happens for tree_height(None) which returns 0 as here the node is None this gets returned to call 2 which becomes 1 + max(1,tree_height(None)) then call 2.2 happens which also returns 0 and now our total return value of whole call 2 becomes 1 + 0 + 0 = 1 so 1 gets returned back to call 1 and it makes our line in call 1 = 1 + max(1,tree_height(3))

# now call 3 happens for tree_height(3) and inside it execution of 2nd return statement happens which makes the line = 1 + max(tree_height(None), tree_height(None)) then internal 3.1 and 3.2 calls happen and they return 0 , 0 and that makes our whole call 3 value be 1 + 0 + 0 = 1 and 1 gets returned back to call 1 which makes it 1 + max(1,1) and since both inside max are 1 so we take 1 which makes our expression 1 + 1 = 2 as our answer


def tree_size(node): # This function takes a node and returns the total number of nodes in the tree rooted at that node
    if node is None: # base case
        return 0
    return 1 + tree_size(node.left) + tree_size(node.right) # recursive case that means size is 1 for current node + size of left subtree + size of right subtree

print(tree_size(tree3))
print(tree_size(tree2))
print()


# for tree3 call 1 happens and 2nd return statement gets executed that makes our line = return 1 + tree_size(2) + tree_size(3) now we pause here

# call 2 happens for tree_size(2) and here also 2nd return statement gets executed that makes the line = return 1 + tree_size(None) + tree_size(None) and then this pauses and call 2.1 and 2.2 happens which return 0,0 as the node is None and that makes our return expression of call 2 as 1 + 0 + 0 = 1 and this gets returned back to call 1 which makes call 1 line = return 1 + 1 + tree_size(3)

# now call 3 happens for tree_size(3) again its 2nd return statement gets executed which makes it return 1 + tree_size(None) + tree_size(None) which then pauses here and call 3.1 and 3.2 happens and returns 0,0 that makes our call 3 return expression as 1 + 0 + 0 = 1 which gets returned to call 1 and that makes its return expression as 1 + 1 + 1 = 3 as the final answer 


# Now we will combine all functions that we have written so far in class TreeNode


class TreeNode:
    def __init__(self,key):
        self.key = key
        self.right = None
        self.left = None
    
    def height(self):
        if self is None:
            return 0
        return 1 + max(TreeNode.height(self.left),TreeNode.height(self.right))
    
    def size(self):
        if self is None:
            return 0
        return 1 + TreeNode.size(self.left) + TreeNode.size(self.right)
    
    def traverse_inorder(self):
        if self is None:
            return []
        return (TreeNode.traverse_inorder(self.left) + [self.key] + TreeNode.traverse_inorder(self.right))
    
    def traverse_preorder(self):
        if self is None:
            return []
        return ([self.key] + TreeNode.traverse_preorder(self.left) + TreeNode.traverse_preorder(self.right))
    
    def traverse_postorder(self):
        if self is None:
            return []
        return (TreeNode.traverse_postorder(self.left) + TreeNode.traverse_postorder(self.right) + [self.key])
    
    def display_keys(self, space='\t', level=0):
        # If the node is empty
        if self is None:
            print(space*level + '∅')
            return   

        # If the node is a leaf 
        if self.left is None and self.right is None:
            print(space*level + str(self.key))
            return

        # If the node has children
        display_keys(self.right, space, level+1)
        print(space*level + str(self.key))
        display_keys(self.left,space, level+1)

    def to_tuple(self):
        if self is None:
            return None
        if self.left is None and self.right is None:
            return self.key
        return TreeNode.to_tuple(self.left),  self.key, TreeNode.to_tuple(self.right)
    
    def __str__(self):
        return f"Binary Tree:{self.to_tuple()}"
    
    def __repr__(self):
        return f"Binary Tree:{self.to_tuple()}"

    def parse_tuple(data):
        if data is None:
            node = None
        elif isinstance(data, tuple) and len(data) == 3:
            node = TreeNode(data[1])
            node.left = TreeNode.parse_tuple(data[0])
            node.right = TreeNode.parse_tuple(data[2])
        else:
            node = TreeNode(data)
        return node
    
tree2 = TreeNode.parse_tuple(tree_tuple)
print(tree2)
print()

print(tree2.display_keys())
print('\n')
print('\n')

print(tree2.size())
print()
print(tree2.height())
print()

print(tree2.traverse_inorder())
print()
print(tree2.traverse_preorder())
print()
print(tree2.traverse_postorder())
print()

print(tree2.to_tuple())
print()




# Binary Search Tree

#  A binary search tree is a binary tree where every node follows a special ordering rule that makes search faster 

# A general binary tree just have the structure rule that each node have a left and right child that's it there is no way for us to apply the binary search logic on a tree that can have random nodes everywhere so a general binary tree is not good for applying the search logic

# That's where the binary search tree comes in place with some additional rules that for every node all values in the left subtree must be smaller and all values in the right subtree must be larger and this must be true for every single node

bst_tree0 = """
        50
       / \
      30  70
     / \ / \
    20 40 60 80
"""

# This property of binary search tree makes operations like insertion, update, search and sorted traversal easy and efficient than binary trees.

# QUESTION: Write a function to check if a binary tree is a binary search tree (BST).

# QUESTION: Write a function to find the maximum key in a binary tree.

# QUESTION: Write a function to find the minimum key in a binary tree.

# These are some questions we need to answer to understand about binary search trees and we will be doing that by writing just one function that encapsulates all of the answers

def remove_none(nums):
    return [x for x in nums if x is not None]
# This helper function is used for removing None values from a given argument because when we calculate max and min None interferes with the logic of finding the min value so we remove it to get accurate data

def is_bst(node): # Base case when tree is empty and we designate it as BST having no min and max values 
    if node is None:
        return True, None, None
    
    is_bst_l, min_l, max_l = is_bst(node.left) # ask left subtree are you a bst and what are your min and max values 
    is_bst_r, min_r, max_r = is_bst(node.right) # ask right subtree are you a bst and what are your min and max values 

    is_bst_node = (is_bst_l and is_bst_r and (max_l is None or node.key > max_l) and (min_r is None or node.key < min_r))

    # This is to check the current node with certain conditions which are:-

    # 1. is_bst_l and is_bst_r :- we are checking if both subtrees are BSTs

    # 2. max_l is None or node.key > max_l :- we are checking either max value of the left subtree is None or the node.key that we are currently on is greater than the max value of the left subtree and to put it simply we are checking that the current node must be greater than everything in the left subtree

    # 3. min_r is None or node.key < min_r :- we are checking that the current node must be smaller than everything in right subtree

    min_key = min(remove_none([min_l,node.key,min_r])) # to get smallest value of the whole subtree
    max_key = max(remove_none([max_l,node.key,max_r])) # to get the largest value in the whole subtree

    return is_bst_node, min_key, max_key

print(is_bst(tree2))
print('\n')
print('\n')

tree4 = TreeNode.parse_tuple((('aakash', 'biraj', 'hema')  , 'jadhesh', ('siddhant', 'sonaksh', 'viru')))

print(display_keys(tree4))
print('\n')
print('\n')

print(is_bst(tree4))
print()


# Storing key value pairs in binary search trees 

class BSTNode():
    def __init__(self,key,value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

# Now we will create a BST with usernames from before as keys and user objects as values 

bst_tree1 = """
        jadhesh
       /       \
    biraj     sonaksh
    /   \      /    \
aakash hema siddhant viru
"""

tree5= BSTNode(jadhesh.username,jadhesh)
print(tree5.key,tree5.value)
print()

tree5.left = BSTNode(biraj.username,biraj)
tree5.right = BSTNode(sonaksh.username,sonaksh)

print(tree5.left.key,tree5.left.value)
print()

print(tree5.right.key,tree5.right.value)
print()

tree5.left.left = BSTNode(aakash.username,aakash)
tree5.left.right = BSTNode(hema.username,hema)

print(tree5.left.left.key,tree5.left.left.value)
print()

print(tree5.left.right.key,tree5.left.right.value)
print()

tree5.right.left = BSTNode(siddhant.username,siddhant)
tree5.right.right = BSTNode(viru.username,viru)

print(tree5.right.left.key,tree5.right.left.value)
print()

print(tree5.right.right.key,tree5.right.right.value)
print('\n')
print('\n')


display_keys(tree5)
print('\n')
print('\n')

print(tree_height(tree5))
print(tree_size(tree5))
print()

# Insertion into an BST

# Write a function to insert a new node in the BST

# We can use the BST property to perform insertion effectively

# 1. Starting from the root node we compare the key to be inserted with the current nodes key

# 2. If the key is smaller, we recursively insert it into the left subtree if its present or attach it as left child if no left subtree exists 

# 3. If the key is larger, we recursively insert it into the right subtree if it exists or attach it as right child if no right subtree exists 


def insert(node,key,value):
    if node is None: # when we find there is no node
        node = BSTNode(key,value) # we make a new node
    
    elif key < node.key: # condition to check if the new key is smaller than root node, and if yes we go left of it
        node.left = insert(node.left,key,value) # as insert takes 3 arguments we are giving it a node(node.left), a key(key) and a value(value)
        node.left.parent = node

    elif key > node.key:
        node.right = insert(node.right,key,value)
        node.right.parent = node

    return node

chirag = User('chirag', 'Chirag parswan', 'chirag@example.com')


tree5 = insert(tree5,chirag.username,chirag)

display_keys(tree5)
print('\n')
print('\n')


tanya = User('tanya', 'tanya gulati', 'tanya@example.com')

tree5 = insert(tree5,tanya.username,tanya)

display_keys(tree5)
print('\n')
print('\n')

print(tree_height(tree5))
print('\n')


# Order of insertion of nodes changes the structure of the resulting tree as we will see in the example below 


tree6 = insert(None, aakash.username, aakash)
insert(tree6, biraj.username, biraj)
insert(tree6, hema.username, hema)
insert(tree6, jadhesh.username, jadhesh)
insert(tree6, siddhant.username, siddhant)
insert(tree6, viru.username, viru)


display_keys(tree6)
print('\n')
print('\n')

print(tree_height(tree6))
print('\n')



# Tree6 came out as skewed and unbalanced tree and that is a problem.

# skewed and unbalanced trees are bad because height stops growing logarithmically that means slowly instead it grows linearly as in our example tree5 and tree6 are basically similar but height of tree5 is 4 and height of tree6 is 6 and nodes are also 6 so height increases linearly here.

# And due to this the length traversed by insert became equal to height of tree in worst case scenario and that makes the time complexity of insertion O(N) in our skewed and unbalanced binary search trees instead of O(log N) in case of a balanced search tree 



# Finding a node in BST

# Write a function to find the value associated with a given key in the BST

def find(node,key):
    if node is None:
        return None
    if key == node.key:
        return node
    if key < node.key:
        return find(node.left,key)
    if key > node.key:
        return find(node.right,key)
    
node = find(tree5, "chirag")

if node is not None:
    print(node.value.name)
else:
    print("User not found")

node = find(tree5, "chirag")

if node:
    print((node.key, node.value))
else:
    print("User not found")

print()


# Updating a value in BST

# Write a function to update the value associated with a given key within a BST

def update(node, key, value):
    target = find(node, key)
    if target is not None:
        target.value = value

update(tree5, 'chirag',User('chirag','chirag pandit','chirag@example.com'))

node = find(tree5, "chirag")

if node:
    print((node.key, node.value))
else:
    print("User not found")

print('\n')
print('\n')


# List the nodes 

# write a function to retrieve all key value pairs stored in BST in sorted order of keys

def list_all(node):
    if node is None:
        return []
    return list_all(node.left) + [(node.key, node.value)] + list_all(node.right)

print(list_all(tree5))
print('\n')
print('\n')





# Balanced Binary trees

# Write a function to determine if a binary tree is balanced 

def is_balanced(node):
    if node is None:
        return True, 0
    balanced_l, height_l = is_balanced(node.left) # ask the left subtree are you balanced and what is your height 
    balanced_r, height_r = is_balanced(node.right)
    balanced = balanced_l and balanced_r and abs(height_l - height_r) <=1 # checking the current node and this means the node is balanced if the left and right subtrees are balanced and difference of height of left and right is less than or equal to 1 as more height will signify that te tree is skewed on one side 
    height = 1 + max(height_l, height_r)
    return balanced, height


print(is_balanced(tree5))
print()
print(is_balanced(tree6))
print('\n')
print('\n')




# Balanced binary search trees 

# Write a function to create a balanced BST from a sorted list/array of key value pairs 

def make_balanced_bst(data,lo=0,hi=None,parent=None): # we are building a balanced binary tree from a sorted list where middle element becomes the root and left and right sides becomes left and right subtrees respectively 
    if hi is None: # setting up hi 
        hi = len(data) - 1
    if lo > hi: # base case when no elements are left
        return None
    
    mid = (lo+hi) // 2 # getting mid
    key,value = data[mid] # getting key and value of mid element 

    root = BSTNode(key,value) # creating a node 
    root.parent = parent
    root.left = make_balanced_bst(data,lo,mid-1,root) # building left subtree
    root.right = make_balanced_bst(data,mid+1,hi,root) # building right subtree

    return root

data = [(user.username, user) for user in users]


tree7 = make_balanced_bst(data)
display_keys(tree7)

print('\n')
print('\n')


# Balancing an unbalanced binary tree

# We will first perform an inorder traversal, then create a balanced BST using the function defined earlier.

def balanced_bst(node):
    return make_balanced_bst(list_all(node))

tree8 = None
for user in users:
    tree8 = insert(tree8, user.username, user)

display_keys(tree8)
print('\n')
print('\n')


tree9 = balanced_bst(tree8)

display_keys(tree9)
print('\n')
print('\n')


# After every insertion, we can rebalance the BST to keep it from becoming skewed, but this comes with a tradeoff: insertion itself is fast (O(log N) in a balanced tree), but rebalancing requires converting the tree to a sorted list and rebuilding it, which takes O(N), making each such insertion effectively O(N). However, the benefit is that future operations like find and update remain very fast at O(log N), because the tree stays short and balanced. The key improvement between O(N) and O(log N) is massive in practice—for example, with 100 million elements, a linear search might take up to 100 million steps, whereas a balanced BST reduces this to about 26 steps (log₂N), which is thousands to millions of times faster. Because balancing every single time is expensive, a practical strategy is to rebalance occasionally (e.g., after many insertions or periodically), so most insertions remain fast while still keeping the tree efficient overall.