# Write a program to sort a list of numbers 

# Sorting usually means sorting in ascending order unless specified 

# And after we have built some foundational knowledge about sorting algos we will answer this question :-

# Q. You're working on a new feature on Jovian called "Top Notebooks of the Week". Write a function to sort a list of notebooks in decreasing order of likes. Keep in mind that up to millions of notebooks can be created every week, so your function needs to be as efficient as possible.

# To put it clearly the problem we are solving is that we need to sort the numbers in a given list in increasing order

# The input looks like this :- nums = [4,2,6,3,4,6,2,1] and the output should look like this :- sorted_list = [1,2,2,3,4,4,6,6] and the function should look like this :- def sort(nums):

# Now we will come up with some examples of inputs and outputs 

# test case 0 :- List of numbers in random order

test0 = {
    'input': {
        'nums': [5, 2, 6, 1, 23, 7, -12, 12, -243, 0]
    },
    'output': [-243, -12, 0, 1, 2, 5, 6, 7, 12, 23]
}

# test case 1 :- a list that is already sorted 

test1 = {
    'input': {
        'nums': [3, 5, 6, 8, 9, 10, 99]
    },
    'output': [3, 5, 6, 8, 9, 10, 99]
}

# test case 2 :- a list that is sorted in descending order

test2 = {
    'input': {
        'nums': [99, 10, 9, 8, 6, 5, 3]
    },
    'output': [3, 5, 6, 8, 9, 10, 99]
}

# test case 3 :- list containing repeating elements 


test3 = {
    'input': {
        'nums': [5, -12, 2, 6, 1, 23, 7, 7, -12, 6, 12, 1, -243, 1, 0]
    },
    'output': [-243, -12, -12, 0, 1, 1, 1, 2, 5, 6, 6, 7, 7, 12, 23]
}

# test case 4 :- An empty list 
 
test4 = {
    'input': {
        'nums': []
    },
    'output': []
}


# test case 5 :- A list just containing one element 


test5 = {
    'input': {
        'nums': [23]
    },
    'output': [23]
}

# test case 6 :- A list containing a single element repeated many times


test6 = {
    'input': {
        'nums': [42, 42, 42, 42, 42, 42, 42]
    },
    'output': [42, 42, 42, 42, 42, 42, 42]
}

# test case 7 :- A really long list.

import random

in_list = list(range(10000))
out_list = list(range(10000))
random.shuffle(in_list)

test7 = {
    'input': {
        'nums': in_list
    },
    'output': out_list
}

tests = [test0,test1,test2,test3,test4,test5,test6,test7]


# Now to come up with a solution 

# 1. iterate over the list
# 2. compare each number with the number it follows 
# 3. If the number we are at is greater than the number it follows we swap the the elements 
# 4. We repeat steps 1 to 3 till the whole list is sorted 



# The solution we are implementing is called bubble sort

# Bubble sort :- When we start iterating on our list and compare each number with the number it follows and swap the elements where the number we are at is greater than the number that follow certain things happen after each iteration the largest unsorted number moved to the left of the list or should we say the largest number in the list reaches its final correct position and after each iteration the unsorted region keeps shrinking like depicted below

# Pass 1:
# [ ? ? ? ? | 9 ]

# Pass 2:
# [ ? ? ? | 8 9 ]

# Pass 3:
# [ ? ? | 7 8 9 ] 

# We keep repeating steps 1 to 3 till n-1 times because at that point all the big elements are sorted and the only remaining smallest element is already at the place so that whole list fulling being sorted 

# Its called bubble sort because smaller elements slowly moves left and larger elements which we call 'bubbles' and they keep moving towards the right of the list which depicts how bubbles rise in the water



# Implementation of bubble sort

def bubble_sort(nums):
    nums = list(nums)
    for _ in range(len(nums)-1): # Outer loop to specify how many times loop should run
        for i in range(len(nums)-1): # inner loop to do the work on each iteration
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
    return nums


nums0, output0 = test0['input']['nums'], test0['output']

print()

print('Input:', nums0)
print('Expected output:', output0)
result0 = bubble_sort(nums0)
print('Actual output:', result0)
print('Match:', result0 == output0)

print()


# Function for visual display of results of tests


import time

def evaluate_test_case(func,test,display=True,):
    inputs = test["input"]
    expected = test["output"] 
    start = (time.time()) 
    actual = func(**inputs) 
    end = (time.time())  

    exec_time = (end- start) * 1000
    passed = (actual == expected) 

    if display:
        print("Input:", inputs)
        print("Expected output:", expected)
        print("Actual output:", actual)
        print("Execution time:", round(exec_time, 4), "ms")  
        print("Test result:","PASSED" if passed else "FAILED")
           
        print()

    return actual, passed, exec_time

def evaluate_test_cases(func, tests, display=True):
    total = len(tests)  
    passed = 0 
    failed = 0  
    for i, test in enumerate(tests):
        print(f"Test case {i}")
        _, test_passed, _ = evaluate_test_case(func,test,display=display)
        if test_passed:  
            passed += 1
        else:
            failed += 1
    print("SUMMARY")
    print(f"TOTAL:{total}, PASSED:{passed}, FAILED:{failed}")


results = evaluate_test_cases(bubble_sort,tests[:6])



# Analyzing the complexity 

# Bubble sort mainly do 2 main operation 
# 1. comparison  2. swapping

# To analyze the complexity we only take comparisons into consideration because every swap requires a comparison first bu not every comparison requires a swap, so comparisons are a guaranteed repeated work 

# The outer loop as well as inner loop does n-1 work. For every outer loop pass the inner loop scans the list again so our work becomes (n-1) * (n-1) 
# And that inturn becomes (n-1)² and according to algebra when we expand on it with the rule (a-b)² = a² -2ab + b² it becomes (n-1)² = n² - 2n + 1

# In BigO notation we ask the question as input becomes huge with term dominates the growth and in our case of (n-1)² = n² - 2n + 1 . The n² dominates the growth as if the number n = 1,000,000 becomes n² = 1,000,000,000,000 the number -2n + 1 is tiny compared to that so we dont take that into consideration 

# Thus our Time complexity becomes O(n²) . First i will define what is quadratic, in maths quadratic means an polynomial equation or expression where the highest power of a variable is ² . In our case a quadratic time complexity means an algorithm whose execution time grows in proportion to the square of the input size.

# Thats why bubble sort is not used in massive data sets as work increases proportional to ² of input size 






