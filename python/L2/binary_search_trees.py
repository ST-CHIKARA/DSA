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

