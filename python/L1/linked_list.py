# Linked list are a type of data structure that stores each element in a list in a separate object called a node. 

# A node is made up of 2 things the element itself and the reference to the next item/element in list. The first node in the linked list is called Head and the last one is called Tail and generally a linked list only maintains a reference to the head. Every node other than the tail points to the next node on the list and thats how we know tail is the end of the list.

# Nodes are called self referential objects :- simply put a node referring to other node or to be technical:- an object that contains a reference to an object of its own class/type

# Linked list are of 2 types :-
# 1. singly linked list :- where each node stores a reference to the next node 
# 2. doubly linked list :- where each node stores a reference to both the node before and after 

# If array's are like bogeys of a train a linked list is like a treasure hunt where at the start of the hunt you have a piece of paper with the location of the 1st treasure, you go to that location and you find a item along with the location of next item of treasure and when you find a item that doesn't also include a location to next item you know the hunt is ended

class Node():
    """
    An object to store a single node of a linked list.
    Models two attributes - data and the link to the next node in the list 
    """
    data = None
    next_node = None

    def __init__(self,data):
        self.data = data

    def __repr__(self): # string representation for ease of debugging and testing
        return f"<Node data: {self.data}>"
    
    # def __str__(self): # str method for printing in a human friendly way 
    #     return f"Node contains {self.data}"
    
# we can either interact with this class in the terminal by using cmd python3 -i linked_list.py which will open a interactive python shell in the terminal and we can interact with the class like making a class object by doing n1 = Node(10) and then writing n1 in the terminal to see what that object is and represent it in string for human understanding with the help of __repr__ . This is usually used to test objects in terminal 

# I also added a __str__ method for another string representation as it is used by print() and if its not present print() can also use __repr__ as a fallback for string representation 

n1 = Node(10)
print(n1) 
print()

n2 = Node(20)
print(n2)
print()

n1.next_node = n2
print(f"n1 points to n2 with {n1.next_node} ")
print()

class Linked_List:
    """
    singly linked list
    """

    def __init__(self):
        self.head = None # we have set the default value of head as none because every new list we make is always empty.
        # I have not defined the head attribute in the class but instead inside the initializer constructor which will still assign a head attribute for each object created 
   

# A common operation used on data structures is to check whether it have some data in it or is it empty 

    def is_empty(self): # to check if our data structure is empty 
        return self.head == None # will return True if list is empty otherwise False 
    
    def size(self):
        """
        Returns the number of nodes in the list 
        runs O(n) linear time complexity
        """

        current = self.head
        count = 0

        while current != None:
            count += 1
            current = current.next_node # we assigned the next nodes direction to current which is initially head so head becomes a node that have data and reference to next node
            # and when current becomes None at the tail while loop terminates 
        return count 
    

l = Linked_List()
l.head = n1
print(l.size()) # will show 2 as the output because we have reference to n2 in the n1 
print()

# prepend :- added to front (HEAD)
# append :- added to end (TAIL)

# adding data to the linked list is efficient only if we are adding it to head or tail namely prepend and append and it is not inserting

# inserting would be to add data in places other than the head or tail

# since a linked list only keep a reference to the head and to add to the tail we have to traverse the list we will be adding data to the head 


def add(self,data):
    """
    adds a new node at the head of the list 
    take O(1) constant time because we are not traversing yet we are just adding at the head 
    """
    new_node = Node(data)
    new_node.next_node = self.head
    self.head = new_node

Linked_List.add = add

l.add(5)
print(l.size())
print()


def __repr__(self):
    """
    return string representation of the list
    runs at O(n) linear time complexity
    """
    nodes = [] # empty python list 
    current = self.head # current at head
    while current != None:
        if current == self.head: # when at head
            nodes.append(f"[Head: {current.data}]") # add Head:current data of string to the empty list called nodes
        elif current.next_node == None: # if at node which is None which means at the tail 
            nodes.append(f"[Tail: {current.data}]") # add Tail: current data to the nodes
        else: # if not at head or tail 
            nodes.append(f"[{current.data}]") # add current data to the list 
        current = current.next_node # at every iteration we will move the current forward to next node and reassigning it 
    return "->".join(nodes)

Linked_List.__repr__ = __repr__

print(l)
print()


def search(self,key):
    """
    search for the first node containing data that matches the key 
    returns the node or None if not found
    takes O(n) time
    """
    current = self.head
    while current != None: # can be written as while current: 
        if current.data == key: # check if the value is at head 
            return current # we return the value
        else:
            current = current.next_node # jump to next_node
    return None # if the loop reaches the tail and tail is also not the key 

Linked_List.search = search

l.add(30)
print(l)
print()

s1 = l.search(20)
print(s1)
print()

s2 = l.search(35)
print(s2)
print()


# insert/deletion in a linked list

# While inserting and deleting can be done at O(1) time finding the position at which the insertion or deletion is to take place takes O(n) time (traversal) 

# INSERTION

def insert(self,data,index): # while linked list have nodes and not index we can mimic that behavior by just counting the number of times we have accessed the next node. for example if we pass index value as 0 it means we are trying to add the data at the head of the list
    """
    inserts a new node containing data at index position 
    insertion takes O(n) but finding the node at the insertion point takes O(n) time 
    therefore it takes a overall O(n) time
    """
    if index == 0:
        self.add(data) # self is the object that is stored in some variable like n1 = Node(10)
    if index > 0:
        new = Node(data) # create a new node with the data to be inserted

        position = index # we are using position as a variable that stores the index we will give as a argument
        current = self.head # starting position

        while position > 1: # this condition is here so that we can stop at the node index before the target index to rewire the pointers because to insert at index i, stop at index i-1(will explain this with a example below)
            current = current.next_node # we traverse the the next node after the head (open the node box and look what it points to next)
            position -= 1 # decrement the position 
            
            prev_node = current # prev_node contains the node we are currently standing on which will be before the new node that will be inserted 
            next_node = current.next_node # this means take whatever is in the current.next_node and put it in the variable next_node

# A mistake i made here previously was i indented the below written insertion logic inside the above written traversal logic and that caused insertion before traversal was complete and gave our wrong out but now i corrected it             

        prev_node.next_node = new # we rewire the prev_node pointer to the new node we inserted 
        new.next_node = next_node # here we are rewiring the pointer of the new node that we just inserted after the prev_node to the next_node variable which inside it stores a node object that we got from current.next_node and stored it in the variable called next_node (will explain with an example)

Linked_List.insert = insert

i1 = l.insert(15,3)
print(l) # output :- [Head: 30]->[5]->[10]->[15]->[Tail: 20]
print()

# To explain things how the above written insert code worked is like this :-
 
# we had a linked list (l) having the data :- [Head: 30]->[5]->[10]->[Tail: 20] and i wanted to insert the [15] after [10] and before the [Tail: 20] so we gave the insert function the arguments (15) which is the data and (3) which is the index 

# we are counting index from 0 so at (0 its 30 , 1 its 5, 2 its 10 and at 3 its 20) 

# TRAVERSAL STEP :-

# As our index argument is not 0 the condition where we can add at the head is skipped and we enter the condition that executes when index > 0, now we make a new node that is to be inserted which is 15 
# index is stored inside the variable position there and we have a variable called current that stores the head reference which is 30

# now our condition while position > 1 is executed and it is true as currently our position is 3 so 3>1 we move to current = current.next_node which is 5 so now our current is at 5 then we decrement the position in next line and it becomes 3-1=2. now we check the while condition again 2>1 we again move to next position that is 10 and then we decrement the position again and it becomes 2-1=1 and when we again check the while condition 1>1 now it becomes false and we exit out of the while loop 

# now we have initialized 2 variables for 2 different purpose, prev_node is there which holds the node value that we are currently on and in our case its 10 for now and next_node(variable in this case to be specified again) which holds the next node value from the current node value which we get by current.next_node and store in next_node (variable) which in our case is 20

# now we have both the previous node data/pointer and the next node data in between which we have to insert our new node 

# and as i mentioned earlier to insert at index i you stop at index i-1 so in our case we need to insert at index 3 so we stopped at index 3-1=2 which holds 10


# INSERTION STEP :- 

# now we move to the insertion part of the code where we are rewiring the pointers of the prev_node and the new_node 

# 1. prev_node.next_node = new :- what we are doing here is we are telling the pointer of the node which hold 10 at index 2 to refer to the new node which is 15 (here .next_node is the Node class attribute)
# 2. then we take the new.next_node (class Node attribute next_node) which holds 15 and telling its pointer to refer to the next_node(variable) which holds 20 in it which we got from current.next_node(class Node attribute next_node) previously

# and now we have successfully inserted our new node at the position we wanted it to be inserted and our output becomes    [Head: 30]->[5]->[10]->[15]->[Tail: 20]


# DELETION

def remove(self,key):
    """
    removes the node containing the data that matches the key
    returns the node or none if the key doesn't exist 
    takes O(n) time [worst case scenario]
    """
    current = self.head
    previous = None # to keep track of the previous node as we traverse and as we start from head it doesn't have a previous position so we start previous with None
    found = False # will serve as stopping condition for the loop that we will define we will traverse the loop till the found is False and we will set it up as true when the key is found, to put it simply it just keep searching until told otherwise 

    while current and not found: # to put it simply it means keep looping until there is a current node to check (current != None) and we haven't found the value yet meaning and this applies only to the logic of the loop here :- when we have initialized found = False and then we write not found that flips the boolean and makes not found = True which essentially here mean we still haven't found our key yet so keep going. for example if we are trying to find (x) and we are going through each node and we still haven't found (x) keep going and when we find our (x) found becomes True as it will be returned below this makes our not found into False which means the condition for the loop as we previously emphasized on cant be fulfilled now so we exit the loop 
    # and to put it in beginner perspective we can write it as :- 
    # while current is not None (meaning != None) and found == False:
        if current.data == key and current is self.head: # condition if the data we want to remove is at head 
            found = True # key found 
            self.head = current.next_node # update the head to next_node so that it becomes the head as head is deleted 
        elif current.data == key: # condition when you find the key during traversal which means it is not the step if you dont find your data at head instead you move to else first 
            found = True # key found
            previous.next_node = current.next_node # to make the previous node connect to next node by skipping the key we just found and just connecting the previous node with the next_node in the linked list 
            # We don’t delete nodes directly, we just change the connections so the node is no longer part of the list.
        else:
            previous = current # if data not at head we make the previous which was None to current 
            current = current.next_node # and current to next_node 
            # these 2 steps happen till we fulfill the condition where current.data becomes equal to key (the elif statement )
    return current # returns the node that was removed 


Linked_List.remove = remove

r1 = l.remove(20)
print(l) # output :- [Head: 30]->[5]->[10]->[Tail: 15]
print()

# To explain how we removed 20 using above written function goes like this :- 

# currently our linked list is [Head: 30]->[5]->[10]->[15]->[Tail: 20] so to remove 20 we first need to find 20 in the list and to do that we start with the while loop 

# since we have already defined our current as self.head so we start with head we full fill the condition while current != None and not found as we just started and not found the key yet 

# then we see if current.data == key and current is self.head since 30 != 20 we skip this condition and move to else

# there our previous which was None becomes current with this previous = current and that makes previous(None) = 30 and in next line makes current = current.next_node which makes it 30 -> 5 , now our previous is 30 and current is 5 we have moved in the list to another node 

# we now check the elif statement to see if we got to our key but again the condition turns false as current.data which is 5 != 20 

# we again come to else statement and now previous becomes 5 and current becomes 10 

# we again check elif and 10 != 20

# we come back to else which makes our previous = 10 and current = 15 

# elif again not fulfilled as 15 != 20

# then again else , previous becomes 15 and current becomes 20 

# now when we check again the elif statement now it becomes fulfilled as 20 == 20 and we have found our key and found becomes True and we move to next line where previous.next_node which is 15 points to None as current.next_node becomes None as 20 was the Tail node and we connect their pointers or we can say previous node points to None and is rewired and 20 is just skipped/ removed from the list and loop ends 

r2 = l.remove(30)
print(l) # output :- [Head: 5]->[10]->[Tail: 15]
print()

# in this case the 1st condition got fulfilled inside the loop where current.data (30) == key (30) became true and current (30) is self.head (30) became true then we move to next line and say we have found the data = True and then we make self.head the next node by doing self.head = current.next_node and the head gets removed or to be technically correct the previous head is no longer connected to the list so in turn removed 
