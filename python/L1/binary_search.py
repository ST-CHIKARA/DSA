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

#===============================================================================================

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


import time



def locate_card(cards, query):
    pass


# ===============================================================================================

# Step 2:-

# Before we start writing our function we will come up with some examples of inputs and outputs which we will use later to test our problem and we will refer to them as test cases

cards = [13, 11, 10, 7, 4, 3, 1, 0]
query = 7
output = 3

result = locate_card(cards, query)

print(result == output) # will return False as this was just a crude way to understand things as we have not yet implemented our function

# now that we saw a single test case and tested it (crudely) its not enough, we need multiple test cases so we will represent our test cases as dictionaries to make it easier to test them once we complete our function for example the above test can be represented as follows

# 0 test case

test = {"input": {"cards": [13, 11, 10, 7, 4, 3, 1, 0], "query": 7}, "output": 3}

# each test case will have 2 main keys input and output and input will have 2 keys within it specifying the arguments that will be fed into the function.

print(locate_card(**test["input"]) == test["output"])
print()

# our function should be able to handle any set of valid inputs that we pass into it and here are the list of some possible variations that we may encounter and these variations will include edge cases too which means variations that are rare and extreme for eg:- we dont have query as the input or the list of cards is empty

# we will store all our test cases in a list called tests = [] which will help us in easier testing later on

# well add our 1st test case in the list by doing

tests = []
tests.append(test)


# 1st test case
# the number query occurs somewhere in the middle of the list of cards

tests.append({"input": {"cards": [13, 11, 10, 7, 4, 3, 1, 0], "query": 1}, "output": 6})


# 2nd test case
# query is the 1st element in the list of cards

tests.append({"input": {"cards": [4, 2, 1, -1], "query": 4}, "output": 0})


# 3rd test case
# query is the last element in the list of cards

tests.append({"input": {"cards": [3, -1, -9, -127], "query": -127}, "output": 3})


# 4th test case
# list of cards just contain one element which is query

tests.append({"input": {"cards": [6], "query": 6}, "output": 0})


# 5th test case
# what if the query is not present in the list of cards we will assume the function will return or we can say the output in this case will be -1

tests.append({"input": {"cards": [9, 7, 5, 2, -9], "query": 4}, "output": -1})


# 6th test case
# list of cards is empty here also we will assume out output to be -1

tests.append({"input": {"cards": [], "query": 7}, "output": -1})


# 7th test case
# the list cards contain repeating numbers

tests.append(
    {
        "input": {"cards": [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], "query": 3},
        "output": 7,
    }
)


# 8th test case
# the query occurs at more than one position in the list cards:- in this case we want out output to be deterministic which means we want a single correct answer not a random one and as you access elements in the list and we go through list the seeking of the element stop at the 1st occurrence of the element we are seeking so we will make out output in this context

tests.append(
    {
        "input": {"cards": [8, 8, 6, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 1], "query": 6},
        "output": 2,
    }
)


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


def locate_card(cards, query):
    # create a variable position with value 0
    position = 0

    # set up the loop that will iterate through the list cards and check out conditions

    while True:

        # check if the element at the current position matches the query
        if cards[position] == query:
            # if this returns True we return the position
            return position
        # otherwise we increment the position
        position += 1  # this is our else statement here what this block does is we check the element at current position against the query if true return position otherwise increment position and check again

        # this was applicable if the query is in cards, if the case is opposite that means the query is not in the cards we check if we have reached the end of list by doing

        if position == len(cards): # we reach here when the upper block of code have exhausted its indexes and as we are incrementing the position when we exhaust our index the next value comes here as we exit out of the upper loop and we compare that is the position == length of our list and if that is true we return -1 and that represents that:-
            return -1  # return -1 when we didnt find the query


print(locate_card(test["input"]["cards"], test["input"]["query"]))
    # what this line does is something called accessing the nested data structure and since we are working with a dictionary its called nested dictionary access. as our function needs 2 arguments namely cards and query and we have our test case structure already mapped out previously in form of nested dictionaries when we write test['input']['cards'] it is like pulling out values out of a box test is the main box inside it is input so we open the input box input has 2 keys cards and query so firstly we open cards box and take out its value and feed it to the function now the 1st argument called cards have a value and our function can access it, now the next test['input']['query'] also behaves the same way we open test inside we see input and inside that we see query we take out that value and feed it to the function. now our function have both the arguments it needs to execute

print(locate_card(**test["input"]))
    # we can write the above nested dict accessing like this way like we wrote earlier way above in the starting what ** does is that it unpacks the dictionary into keyword arguments like they are in the nested structure as inside input there is cards and query and python converts this locate_card(**test['input']) into this locate_card(cards=[13,11,10,7,4,3,1,0], query=7) just like we want

print(locate_card(**test["input"]) == test["output"])
print()


# now that we have our solution we will add HELPER UTILITIES FUNCTIONS to help us test our test cases


# this function is for only 1 test case as we are just trying to build logic on how can we make a function that will help us in evaluating test cases


def evaluate_test_case(func,test,display=True,):
    # func:- func we want to test and display acts like a switch to control whether we want to see detailed output or not (useful especially for large inputs)

    inputs = test["input"]
        # we are extracting the inputs that are cards and query from the test and putting it into the variable inputs which will look something like this (inputs = {'cards':[13,11,10,7,4,3,1,0], 'query':7})
    
    expected = test["output"] 
        # extracting the expected result and putting it into a variable

    start = (time.time()) # returns the current system time as a float measured in sec we are doing this because we want to measure the executing time of our func
    actual = func(**inputs) # this becomes func(unpacking of inputs which we talked about earlier)
    end = (time.time())  # the timer that got started when we did start stops here and now we have a time frame from start to end of the executing

    exec_time = (end- start) * 1000
        # since end and start are in seconds we convert them to milliseconds by multiplying their difference by 1000 because 1 sec = 1000 ms (for eg 0.005sec * 1000 = 5 ms)
    

    passed = (actual == expected) # now we compare our return value of func that is stored in actual with the expected that stores our expected output and then store their comparison result in our variable passed

    # we use display as a control switch so that for normal test cases we can see full details (input, expected, etc.)
    # but for very large test cases we can turn it off (display=False) to avoid printing huge data and cluttering the output

    if display:
        print("Input:", inputs)
        print("Expected output:", expected)
        print("Actual output:", actual)
        print("Execution time:", round(exec_time, 4), "ms")  # rounding the exec_time till 4 decimal places as the exec_time can easily have 10-15 decimal places which are not necessary to us
        print("Test result:","PASSED" if passed else "FAILED")
            # we are using a ternary conditional expression here for writing a if else statement in one line following this syntax (value_if_true if condition else value_if_false)
        print()

    return actual, passed, exec_time


(evaluate_test_case(locate_card, test))
print()


# now we will write a function that can run all test cases at once


def evaluate_test_cases(func, tests):
    for i, test in enumerate(tests): # here we are using the enumerate() func because when we use it, it adds an index infront of each item of an iterable which in our case is tests list having multiple test cases and its returns the index and item as tuple (index,item)
        print( f"Test case {i}")  # will output Test case 1, Test case 2.......... Test case 8
        evaluate_test_case(func, test)


# 2nd iteration of evaluate_test_cases for additional summary(just a visual effect) functionality


def evaluate_test_cases(func, tests, display=True):
    total = len(tests)  # to get total number of tests
    passed = 0  # counter initialization to calculate passed tests
    failed = 0  # counter initialization to calculate failed tests
    for i, test in enumerate(tests):
        print(f"Test case {i}")
        _, test_passed, _ = evaluate_test_case(func,test,display=display)
            # since our evaluate_test_case returns 3 values that are actual,passed and exec_time we only need passed and store it in variable test_passed. here we pass display forward (propagation) so that evaluate_test_case behaves accordingly.if display=True → full details printed and if display=False → only essential output printed (no large input dump)
        
        if test_passed:  # condition for the counter
            passed += 1
        else:
            failed += 1
    print("SUMMARY")
    print(f"TOTAL:{total}, PASSED:{passed}, FAILED:{failed}")


# print(evaluate_test_cases(locate_card,tests))
# print()


# now that we ran our tests we came across an error in test case 6 which says IndexError:list index out of range and that is because in test case 6 we have a empty list and when we try to access it by our locate_card function especially with this line if cards[position] == query: return position when this line executes it finds a empty list and since there is no position to return we come across our error.now to debug this error or should we say this bug we have to write our locate_card function keeping in mind edge cases like this and write it out so that we see what happened and where it happened although we know why the error occurred we can still write our function so that it displays each input that is being fed into the function because when we were testing with evaluate_test_cases as soon as it reached test case 6 it through the error and didnt display the inputs and the expected output we are giving the locate_card func


def locate_card(cards, query):
    position = 0
    print("cards:", cards)
    print("query:", query)
    while True:
        print("position:", position)
        if cards[position] == query:
            return position
        position += 1
        if position == len(cards):
            return -1


cards6 = tests[6]["input"]["cards"]
query6 = tests[6]["input"]["query"]

# print(locate_card(cards6,query6))
# print()


# now to make our locate_card func more robust and accurate in handling the edge cases we will write it like this


def locate_card(cards, query):
    position = 0
    while position < len(cards): # we are checking whether we have reached the end of list before accessing an element from it in this case of position is 0 and len of list is also 0 this condition and code block related to it wont execute and -1 will be returned
        if cards[position] == query:
            return position
        position += 1
    return -1


print(locate_card(cards6, query6))
print()


evaluate_test_cases(locate_card, tests)
print()

# all tests passed and with that one thing becomes clear having multiple test cases was a boon for us without them we may never have discovered the error we faced in test case 6

# all that we learnt till now was to help us understand how to solve a problem but this implementation and testing of brute force solution is usually not done in interviews when we become proficient in solving problems it becomes easy (said by the teacher **haha**) to figure out the time complexity of the brute force solution when stating the solution in simpler terms


# Step 5 :-


# Now we will analyze the algorithm's complexity and identify inefficiencies if any. The question states that Alice wants Bob to pick out the card containing a given number by turning over as few cards as possible. In programming terms we stated this requirement as minimizing the number of times we access elements from the list 'cards'.

# Before we can minimize that number, we need a way to measure it. In our current solution (linear search), we start from the first element in the list and keep checking each card one by one until we find the query.

# If the query happens to be near the beginning of the list, Bob will find it quickly by flipping only a few cards. However, if the query is the last element in the list, or if the query is not present at all, Bob would have to check every card.

# The field of study concerned with finding the amount of time, space, or other resources required to complete the execution of computer programs is called the analysis of algorithms. The process of figuring out the best algorithm to solve a given problem is called algorithm design and optimization.


# COMPLEXITY AND BIG O NOTATION


# Complexity of an algorithm is a measure of the amount of time and/or space required by an algorithm for an input of a given size, usually denoted by N. Unless otherwise stated, the term complexity usually refers to the worst-case complexity, i.e., the highest possible time or space taken by the algorithm to process an input. In our case, the worst case would be Bob flipping every card in the list to find the card he is looking for.

# Worst-case complexity is often expressed using Big O notation.

# Suppose there are N cards on the table. In the worst case Bob may need to access up to N elements from the list before reaching the answer. Because the number of operations grows with the number of cards, we say that the time complexity of linear search is O(N), which is pronounced as "order of N".

# In other words, if the number of cards doubles, the number of checks Bob might need to perform also roughly doubles. Time complexity is sometimes also called the running time of the algorithm.

# To put it more simply, time complexity describes how the amount of work grows when the input size grows. For example, if Bob has 30 cards in front of him and he has to check each of them to find the required number, he may need to perform 30 checks. If the number of cards increases to 50, the number of checks in the worst case also becomes 50. So as the input increases, the work increases proportionally.


# On the other hand, the space complexity of our linear search algorithm depends on how much memory the algorithm uses during its execution. In simpler terms, space complexity tells us how much extra memory the algorithm needs as the input grows.

# Here we are not talking about the memory required by the input itself because the input (the list of cards) already exists before the algorithm starts. Instead, we are only concerned with the extra working memory used by the algorithm.

# In our algorithm we use a few variables such as 'cards' and 'query', which are the inputs provided to the function. Other than these, we only create one additional variable called 'position'.

# No matter how large the input becomes, whether the list contains 30 cards or 300 cards, we still use the same variable 'position' to access elements in the list using the expression (cards[position] == query).

# Whether we are checking cards[3] == query or cards[300] == query, the number of variables used by the algorithm does not increase as the input size grows.

# That is why we say the space complexity of linear search is O(1), which means constant space (or constant memory usage).


# To wrap this up, let's talk about the relationship between input size and the number of steps performed by the algorithm.

# We usually denote the size of the input as N. If the list of cards contains 8 cards, then N = 8. In the worst-case scenario, linear search may need to check all 8 cards before finding the query.

# This means that in the worst case the number of steps performed by the algorithm is proportional to N.

# Sometimes the number of steps is written as cN, where c is a constant that depends on the number of operations performed in each iteration and the time taken to execute each statement.


# When explaining algorithms using Big O notation, we drop fixed constants and lower-order terms in order to capture the overall growth trend of the algorithm.

# For example, suppose algorithm A takes N steps and algorithm B takes 3N steps. If N = 10, then algorithm A takes 10 steps and algorithm B takes 30 steps. Although algorithm A is faster, both algorithms grow linearly with the input size. If the input doubles, the number of steps also doubles in both cases.

# Because both algorithms grow proportionally with N, we describe their time complexity as O(N). Big O notation focuses on the growth pattern of the algorithm rather than small constant differences.


# Before discussing lower-order terms, we need to understand growth in algorithms. Growth refers to how the amount of work changes when the input size increases.

# In linear search we observe linear growth O(N) in time complexity, where the number of steps increases proportionally with the input size. We also observed constant growth O(1) in space complexity, where the memory used by the algorithm remains the same regardless of input size.

# Another common growth pattern is quadratic growth, usually seen when algorithms contain nested loops. In this case the work grows with the square of the input size and is represented as O(N**2).

# For example, suppose an algorithm takes the following number of steps:

# 3N**2 + 5N + 10

# This means:
# 3 × N² operations
# 5 × N operations
# 10 constant operations

# If N = 10:

# 3*(10*10) = 300
# 5*10 = 50
# +10 = 360 steps

# If N = 1000:

# 3*(1000*1000) = 3,000,000
# 5*1000 = 5,000
# +10 = 3,005,010 steps

# As N becomes large, the terms 5N and 10 become very small compared to 3N². They barely affect the total work performed by the algorithm.

# Big O notation therefore focuses on the fastest-growing term. In this case, N² grows much faster than N or any constant value. Therefore the time complexity is written as: O(N²)

# The smaller terms such as N and the constant value 10 are ignored because they have very little impact on the overall growth of the algorithm.


# Step 6 :-

# The solution we implemented works correctly, but only in the case of linear search and it is not the most efficient way to solve the problem. The problem statement tells us to find the number with less number of cards turning and also tells us that the cards are already arranged in decreasing order. This means the data is sorted, and sorted data often allows us to search more efficiently.

# Instead of checking cards one by one, we can use the ordering of the cards to eliminate half of the remaining cards at each step. by this we mean that the next best idea would be to pick a random card, and use the fact that the list is sorted, to determine whether the target card lies to the left or right of it in fact, if we pick the middle card, we can reduce the number of additional cards to be tested to half the size of the list. Then, we can simply repeat the process with each half. This technique is called BINARY SEARCH.

# lets say we have a list which have cards = 9,7,6,4,3,2,1 and the query = 6 and the expected output is 2 which is the position where the 6 is at in the list now how do we find 6 with the least turning of cards? thats where binary search comes in handy as we know that our list is sorted in decreasing order total positions in the list is 6, we are referring position because we access the elements with the help of position (**we can simplify this by saying the list has 7 elements but i found the position as a more simpler way to explain my understanding**). As there as 6 position obviously 3 is the middle lets say we accessed the element 3 of the list and saw 4 (**we are obviously checking against query this explanation was just to simplify the procedure.**), as we know the list is sorted 4 is less than 6 so the positions 4,5,6 get invalidated as they only have numbers less than 4 and we are left with the position 0,1,2 that is on the left side of the list. Now we just have to work with left side of the list lets say we again access the middle element of the left side of the list that will be position 1 and at position 1 we find 7  now 7>6 and at position 3 we had 4 which is < 6 so we are only left with position 2 as the only option where 6 can be if it is in the list so now when we check position against query and if there is a number 6 we get returned its position and voila we have solved our question with the least number of flips.


# Step 7 :-

# Now that we have found out a correct technique to implement we repeat steps 3 to 6 and step 3 was come up with a correct solution and state it in plain english

# here is how binary search can be implemented to our solution
# 1. access the middle element of the list
# 2. compare against query and if it matches return the middle position as the answer or,
# 3. if the middle element is less than queried number then search the first half of the list or we can also say left side of the list
# 4. and if it is greater than the queried number then search the second half of the list or we can say right side of the list
# 5. if no more elements remain return -1


# Step 8 :-

# now that we have stated our new solution simply we implement it by writing out our new locate_card function and then test it using our test cases and also fix bugs (complications if any arise)


def locate_card(cards, query):
    lo, hi = 0,len(cards) - 1,
        # here 2 variables are made where lo represents the left boundary of the current search space that is 0 and hi represents the right boundary of the current search space that will be calculated by len(cards) - 1 and the value that we get from it will be stored in hi
    
    while (lo <= hi): # this condition simply means while we have a valid search space continue searching and by a valid search space we mean is that till lo is either smaller or equal to the hi we have a valid search space for eg if lo is 0 and hi is 6 that means we have the whole search space then lo becomes 1 and search space becomes 5 our search space got smaller and with each iteration it becomes smaller
        mid = (lo + hi) // 2  # to get the middle element of the list
        mid_number = cards[mid]  # to access the element
        print("lo:", lo, ",hi:", hi, ",mid:", mid, ",mid_number:", mid_number)

        if mid_number == query:
            return mid
        elif (mid_number < query): # if mid_number is less than query for eg in our previous example mid position was 3 and it have the mid_number 4 in the list and query was 6 this is the code that shows us that scenario. so 4<6
            hi = (mid- 1)
                # now what we are doing here is we are invalidating the second half of the list by shrinking the valid search space as in our example mid = 3 now hi becomes 3- 1 = 2 and our working space shifts from 0-6 to 0-2, we just discarded the second half of the list and will now work with first half. after the execution of this condition the loop goes back to while lo <=hi which becomes 0<=2 then we find middle again 0+2//2 = 1 , then mid_number = cards[1] = 7 then this block turns out false and we move to next conditional statement.
            
        elif mid_number > query:  # 7 > 6 from our example turns out true for this
            lo = (mid+ 1)
                # it becomes lo = 1+1 = 2 and now lo is 2 and hi is 2 # now next iteration of the loop begins while 2<=2 since its true we move forward to finding mid 2+2//2 = 2 now next line becomes mid_number = cards[2] which gives us 6 now when in the conditional statement it is checked if mid_number == query and now its 6 ==6 we get the value of mid which is 2 returned and hence we have solved our problem in the 3rd iteration and solved our problem with less steps.
            

    return -1  # if query not there return -1


print("--BINARY SEARCH TESTS--")
print()
evaluate_test_cases(locate_card, tests)
print()


# ok as we tested the test cases from the total of 9 test cases 8 passed and the last test case test case 8 (counting from 0) failed where the input was 'cards':[8,8,6,6,6,6,6,6,6,3,2,2,2,1],'query':6 and expected output:2. when binary search executed on it what it did was it took the lo=0, hi=13 , mid=0+13//2 = 6 mid_number = cards[6] = 6 , if mid_number == query 6==6 return mid = 6 and voila for binary search the answer is there but we needed the 1st instance where the 6 first occurs that why the expected output is 2 not 6

# so what is the fix for this edge case ?

# when we find that cards[mid] == query we need to check whether the card is the first occurrence in the list and if not we keep checking the previous number and if yes then we have our answer

# we will write a new helper function called test_location for this which will take cards,query and mid as the arguments(inputs)


def test_location(cards, query, mid, debug=True):
    mid_number = cards[mid]
    # debug acts like a switch to control internal tracing of the algorithm, when debug=True we can see how mid and mid_number are changing in each step, and when debug=False (especially for large inputs) we avoid unnecessary prints in the terminal
    if debug:
        print("mid:", mid, ",mid_number:", mid_number)
    if mid_number == query:
        if (mid - 1 >= 0 and cards[mid - 1] == query):
            # 1st condition checks whether a previous position exists or not so we don’t go out of bounds, for eg if mid is 6 then mid-1 = 5 >= 0 is true but if mid is 0 then mid-1 = -1 >= 0 is false, and 2nd condition checks the previous position card with query like if cards[mid-1] == query and if the query is 6 and at cards[5] there is also 6 then we return left, but if this condition comes false then it means we have found the first occurrence of query and we return found
        
            return "left"
        else:
            return "found"
    elif (mid_number < query): # if card < query we return left because if query is 8 and mid_number is 6 as the list is sorted we get to know that we need to move left as left side will have bigger numbers
        return "left"
    else:  # its like saying else: mid_number>query
        return "right"


# now we again simplify our locate card function


def locate_card(cards, query, debug=True):
    lo, hi = 0, len(cards) - 1
    while lo <= hi:
        # debug acts as a switch to control whether we want to see how the search space is shrinking step by step
        # when debug=True we see lo and hi changing, when debug=False (especially for large inputs) we avoid clutter in the terminal output
        if debug:
            print("lo:", lo, ",hi:", hi)
        mid = (lo + hi) // 2
        result = test_location(cards, query, mid, debug) # instead of doing all logic inside locate_card we delegate here

        if result == "found":
            return mid
        elif result == "left":
            hi = mid - 1  # shrink search to left
        elif result == "right":
            lo = mid + 1  # shrink search to right
    return -1


# in our improved version when we test with the edge case and the mid is 6 and at mid the number is also 6 in 1st iteration when we compare it with query and then we compare the previous position to query and we get returned left because on position 5 the card was also 6 we move to the locate_card function straight after this and the condition that gets fulfilled with this is elif result == "left" and it makes hi = 6-1 = 5 now our search space becomes 0-5 when it was 0-13 previously in just one iteration. then in 2nd iteration our mid becomes (0+5)//2 = 2 now mid_number = cards[2] = 6 now we check against query it is indeed 6 == 6 then we check our condition and when cards[mid-1] = cards[2-1] = cards[1] = 8 and 8 == 6 becomes false we know we have found our query is the 1st occurrence in the list and then we come to locate_card our condition if result == "found" becomes true and the mid position gets returned

print("-----AFTER FIXING EDGE CASE-----")
print()
evaluate_test_cases(locate_card, tests)
print()


# Step 9 :-

# Now we will analyze the complexity of the binary search and identify any inefficiencies if any

# Binary search works by repeatedly dividing the search space into half instead of checking elements one by one like linear search, which allows us to eliminate a large number of elements in each step. Because of this, the number of steps required depends on how many times we can divide the input size (N) by 2 until only one element remains. This idea is what we call a logarithm, where log₂(N) simply means how many times we multiply 2 to reach N, or equivalently, how many times we can divide N by 2 to reach 1. The base 2 comes from the fact that in binary search we always split the data into two halves at every step. Since this number grows very slowly even when N becomes very large, the time complexity of binary search is O(log N). On the other hand, the space complexity is O(1) because we only use a fixed number of variables like lo, hi, and mid, and this does not increase with input size. Therefore, binary search is highly efficient for sorted data because it drastically reduces the number of operations while using constant memory.


# Comparison between linear and binary search


def locate_card_linear(cards, query):
    position = 0
    while position < len(cards):
        if cards[position] == query:
            return position
        position += 1
    return -1


large_test = {
    "input": {"cards": list(range(10000000, 0, -1)), "query": 2},
    "output": 9999998,
}


print("-------linear vs binary-------")
print()

result, passed, runtime = evaluate_test_case(locate_card_linear, large_test, display=False)
print(f"Result:{result}\nPassed: {passed}\nExecution time: {runtime} ms")
print()


# result,passed,runtime = evaluate_test_case(locate_card,large_test,display=False,)
# print(f'Result:{result}\nPassed: {passed}\nExecution time: {runtime} ms'))
# print()


result, passed, runtime = evaluate_test_case(
    lambda cards, query: locate_card(cards, query, debug=False),
    large_test,
    display=False)
    # here we are using lambda which acts as a small temporary function when needed instead of defining a whole new function. It has the basic syntax as lambda arguments : expression and here in our code cards and query are arguments and locate_card(cards,query,debug=False) if we try to understand it with a very simple example if lambda x:x+1 what it will do is take x and add 1 to it and return the result and in our code we already have cards and query but we are adding debug=False as a extra which is needed here so that out terminal dont get cluttered by all the print debug. this line gets executed as first in evaluate_test_case we have inputs in which we have cards and query and in actual we have func(**inputs) so with our lambda function here the actual becomes actual = func(cards,query,debug=False) and when our evaluate_test_case get executed it takes locate_card,large_test,display=False as arguments. display=False is for evaluate_test_case and debug=False is for locate_card

print(f"Result:{result}\nPassed: {passed}\nExecution time: {runtime} ms")
print()


# When we compared linear search and binary search using a very large input we observed that binary search is significantly faster (in our case over 50,000 times faster). this happens because linear search checks elements one by one so if the input size increases 10 times the number of operations also increases roughly 10 times (O(N)). on the other hand binary search eliminates half of the search space in each step so even if the input size becomes 10 times larger it only needs a few more steps (around log₂(N) growth, for eg from ~24 steps to ~27 steps which is only about 3 extra operations). this is the key difference between O(N) and O(log N), as N grows large the gap between them becomes huge, which is why binary search scales much better and becomes far more efficient compared to linear search.


# Generic binary search

# by this we mean the general strategy behind binary search which is applicable to a variety of problems :-

# 1. come up with a condition to determine whether the answer lie before,after or at a given position
# 2. retrieve the midpoint and middle element of the list
# 3. if its the answer return the midpoint as the answer
# 4. if it lies before it repeat the search with the 1st half of the list
# 5. if it lies after the midpoint repeat the search with the 2nd half of the list

# Generic code


def binary_search(lo, hi, condition): # new addition (condition) which will be a function
    while lo <= hi:
        mid = (lo + hi) // 2
        result = condition(mid) # instead of writing the logic of comparison we delegate that to another func called condition. Binary search dont know what cards,query,duplicates etc are it just asks condition like hey i am at mid what should i do now and based on the answer we navigate our list whether ans is found at the mid position or we have to go left or right to search
        if result == "found":
            return mid
        elif result == "left":
            hi = mid - 1
        else:
            lo = mid + 1
    return -1


def locate_card(cards, query):
    def condition(mid):  # this is called function closure (a closure in python is a nested function that remembers and has access to the variables from its enclosing(outer func)). Now the question arises why we did this :- we defined the condition inside because we need it to access cards and query but we dont want to pass them everytime
        if cards[mid] == query:
            if mid > 0 and cards[mid - 1] == query:
                return "left"
            else:
                return "found"
        elif cards[mid] < query:  # answer must be on left where bigger numbers are
            return "left"
        else:  # cards[mid]>query
            return "right"  # answer must be on right where smaller numbers are

    return binary_search(0, len(cards) - 1, condition) # binary search calculates mid --> then calls condition , condition uses cards,query and mid and returns found, left or right then again binary adjusts the search range when needed and repeat till the query is found or not.
    # here we learnt a new concept in programming called a HIGHER ORDER FUNCTION. A higher order function is a function that **either** takes another function an argument or returns a function as its result. Here in our binary_search example binary_search is a higher order function that takes condition as a argument (emphasis on **either**). i will add an example of a higher order function that returns a function as its result after the results.


print("----GENERIC BINARY SEARCH TEST RESULTS----")
print()

evaluate_test_cases(locate_card, tests)
print()

# Example of a HIGHER ORDER FUNCTION that returns another function as its result


def multiplier(n):  # higher order function
    def multiply(x):
        return x * n

    return multiply  # returns this (further shown in examples below)


double = multiplier(2)
triple = multiplier(3)

# so in double, when we call multiplier(2) it returns a function multiply that remembers the value of n as 2, and the same happens in triple where n is 3. now when we do :-

print(double(5))  # this will print 10 because inside double is x * 2 and here x is 5 so 5*2 =10
print(triple(5))  # this will give us 15 because inside triple is x * 3 and here x is 5 so 5*3=15

# All comments are there for personal understanding and can be bit imprecise in technical terms but right now understanding is the priority instead of totally technical and precise language.
