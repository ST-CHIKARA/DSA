# The course starts with a question:- Alice has some cards with numbers written on them. She arranges the cards in decreasing order, and lays them out face down in a sequence on a table. She challenges Bob to pick out the card containing a given number by turning over as few cards as possible. Write a function to help Bob locate the card. # visualize 7 cards with only ? on them laying on the table. 

                             # WHY SHOULD ONE LEARN DSA

# 1. it helps you to think about a problem systematically and solve it systematically step by step
# 2. while solving the problems you envision different inputs, outputs, edge cases for the programs which makes it a comprehensive way of solving a problem
# 3. when you understand a problem and try to solve it step by step it helps you understand the problem in a better way and it helps you communicate that to others clearly
# 4. when you understand a problem you can code its solution easily 

              # A SYSTEMATIC STRATEGY TO SOLVE PROBLEMS IS AS FOLLOWS:-

# 1. state the problem clearly in your own words and identify the input and output formats
# 2. try to come up with some examples of inputs and outputs and try to cover all edge cases of them meaning how many inputs and outputs are there of every type
# 3. try to come up with a correct solution for the problem and state it in plain english 
# 4. implement the solution and test it using the example inputs we came up with and if any bugs appear in the output fix them 
# 5. analyze the algorithm's complexity and identify inefficiencies if any 
# 6. apply the right technique to overcome the inefficiency and then repeat steps 3-6

# ===============================================================================================

# SOLUTION

# Step 1 :- 

# Now lets try to state our problem in simple and clear words which will help us find a solution. The problem states that alice has some cards with numbers written on them and she arranges the card in decreasing order so we can represent those sequence of cards as a list of numbers in decreasing order for eg:- [13,11,10,7,4,3,1,0] and as alice tells bob to pick out the card containing a given number by turning over as few cards as possible, turning over a specific card is equivalent to accessing a element from the list using the corresponding position of that element in the list for example in our list above the element 13 is at position 0, 11 is at 1, 10 is at 2, 7 is at 3, 4 is at 4 as in programming the counting starts from 0 not 1. 

# Now that we have stated our problem in simpler terms our problem can now be stated as:- 
# Q. We need to write a program to find the position of a given number in a list of numbers arranged in decreasing order. We also need to minimize the number of times we access elements from the list 

# From what we understood about the problem we can deduct that we have 2 types of input 
# 1. cards:- a list of numbers sorted in decreasing order [13,11,10,7,4,3,1,0]
# 2. query:- a number whose position in the list is to be determined 

# And the output of the problem should be a position:- which is the position of the query in the list of cards 

# for example if we query on which position is number 7 counting from 0 the answer should be 3 so here input was 7 and output was 3

# Based on what we understood we can write a signature of our function which in simpler terms means structure of our function without any code in it 

# name your function and parameters appropriately like written below the function name locate_card properly describes on its own what we are doing and parameter names cards and query themselves represent what they are 

def locate_card(cards,query):
    pass

# ===============================================================================================

# Step 2:- 

# Before we start writing our function we will come up with some examples of inputs and outputs which we will use later to test our problem and we will refer to them as test cases 

cards = [13,11,10,7,4,3,1,0]
query = 7
output = 3

result = locate_card(cards,query)

print(result == output) # will return False as this was just a crude way to understand things as we have not yet implemented our function

# now that we saw a single test case and tested it (crudely) its not enough, we need multiple test cases so we will represent our test cases as dictionaries to make it easier to test them once we complete our function for example the above test can be represented as follows 

# 1st test case 

test = {
    'input':{
        'cards': [13,11,10,7,4,3,1,0],
        'query':7
    },
    'output':3
}

# each test case will have 2 main keys input and output and input will have 2 keys within it specifying the arguments that will be fed into the function.

print(locate_card(**test['input']) == test['output'])
print()

# our function should be able to handle any set of valid inputs that we pass into it and here are the list of some possible variations that we may encounter and these variations will include edge cases too which means variations that are rare and extreme for eg:- we dont have query as the input or the list of cards is empty 

# we will store all our test cases in a list called tests = [] which will help us in easier testing later on 

# well add our 1st test case in the list by doing 

tests = []
tests.append(test)



# 2nd test case 
# the number query occurs somewhere in the middle of the list of cards

tests.append({
    'input':{
        'cards':[13,11,10,7,4,3,1,0],
        'query':1
    },
    'output':6
})


# 3rd test case
# query is the 1st element in the list of cards

tests.append({
    'input':{
        'cards': [4,2,1,-1],
        'query':4
    },
    'output':0
})



# 4th test case 
# query is the last element in the list of cards 

tests.append({
    'input':{
        'cards':[3,-1,-9,-127],
        'query':-127
    },
    'output':3
})


# 5th test case 
# list of cards just contain one element which is query

tests.append({
    'input':{
        'cards':[6],
        'query':6
    },
    'output':0
})


# 6th test case 
# what if the query is not present in the list of cards we will assume the function will return or we can say the output in this case will be -1

tests.append({
    'input':{
        'cards':[9,7,5,2,-9],
        'query':4
    },
    'output':-1
})



# 7th test case 
# list of cards is empty here also we will assume out output to be -1

tests.append({
    'input':{
        'cards':[],
        'query':7
    },
    'output':-1
})



# 8th test case
# the list cards contain repeating numbers

tests.append({
    'input':{
        'cards':[8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query':3
    },
    'output':7
})




# 9th test case
# the query occurs at more than one position in the list cards:- in this case we want out output to be deterministic which means we want a single correct answer not a random one and as you access elements in the list and we go through list the seeking of the element stop at the 1st occurrence of the element we are seeking so we will make out output in this context

tests.append({
    'input':{
        'cards':[8,8,6,6,6,6,6,6,6,3,2,2,2,1],
        'query':6
    },
    'output':2
})


print(tests)
print()


# the main benefits of making these test cases and edge cases within them are we will be able to handle them while writing our code 

# ===============================================================================================

# Step 3:-

# now that we have stated our problem in clear words and came up with a list of various test cases next step is to come up with a solution and state it clearly
 
# when we are writing our solution it may not be the most efficient at the first try and that is totally normal for now what we can do is write out the simplest and the most obvious solution to the problem which generally involves checking all possible answers and it is called the brute force solution 

# first aim for correctness then aim for efficiency 

# here the most simple and obvious solution can be bob can turn cards one by one till he finds the card alice said him to look for which is our query and here is how we can implement it 
# 1. inside our function create a variable called position with value 0
# 2. now check whether number at index position in cards equals to query 
# 3. if it is equal position is the answer and can be returned from the function
# 4. if not we write our code that behaves like this we increment the position by 1 and repeat step 2 if we get our answer step 3 will get executed other wise we repeat step 4 increment position again execute step 2 again we execute the loop till we reach and have checked till the last position 
# 5. and if the number was not found we return -1


# when we are presenting our answer to a interviewer or someone else always say it out loud what solution you came up with and what it does step by step even if the solution you came up with looks too simple as in this scenario what is being tested is your skill to problem solve and sometimes the simple answer is the best answer 


# what we just did is something called linear search algorithm and as the definition of the algorithm states its a step by step instructions to solve a problem or complete a task and thats what we just did we wrote step by step what our function is doing to solve our problem and this is called a linear search because it searches through a list element by element 


# writing is a tool which is linked to thinking clearly if you find some parts of the solution difficult to express it can mean you cant think clearly about it. the more clearly you are able to express your thoughts in writing easier it will be for you to turn it into code


# ===============================================================================================


# Step 4 :- 

# now we will implement our solution by writing out the function we previously left above and test the function using the test cases we made

def locate_card(cards,query):
    # create a variable position with value 0
    position = 0

    # set up the loop that will iterate through the list cards and check out conditions

    while True:

        # check if the element at the current position matches the query
        if cards[position] == query:
            # if this returns True we return the position
            return position
        # otherwise we increment the position 
        position += 1 # this is our else statement here what this block does is we check the element at current position against the query if true return position otherwise increment position and check again 

        # this was applicable if the query is in cards, if the case is opposite that means the query is not in the cards we check if we have reached the end of list by doing

        if position == len(cards): # we reach here when the upper block of code have exhausted its indexes and as we are incrementing the position when we exhaust our index the next value comes here as we exit out of the upper loop and we compare that is the position == length of our list and if that is true we return -1 and that represents that:- 
            return -1 # return -1 when we didnt find the query  


print(locate_card(test['input']['cards'],test['input']['query'])) # what this line does is something called accessing the nested data structure and since we are working with a dictionary its called nested dictionary access. as our function needs 2 arguments namely cards and query and we have our test case structure already mapped out previously in form of nested dictionaries when we write test['input']['cards'] it is like pulling out values out of a box test is the main box inside it is input so we open the input box input has 2 keys cards and query so firstly we open cards box and take out its value and feed it to the function now the 1st argument called cards have a value and our function can access it, now the next test['input']['query'] also behaves the same way we open test inside we see input and inside that we see query we take out that value and feed it to the function. now our function have both the arguments it needs to execute 
print(locate_card(**test['input'])) # we can write the above nested dict accessing like this way like we wrote earlier way above in the starting what ** does is that it unpacks the dictionary into keyword arguments like they are in the nested structure as inside input there is cards and query and python converts this locate_card(**test['input']) into this locate_card(cards=[13,11,10,7,4,3,1,0], query=7) just like we want 
print(locate_card(**test['input']) == test['output'])