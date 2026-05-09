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


results_bubble_sort = evaluate_test_cases(bubble_sort,tests[:6])

print('--------------------------------')
print('\n')



# Analyzing the complexity 

# Bubble sort mainly do 2 main operation 
# 1. comparison  2. swapping

# To analyze the complexity we only take comparisons into consideration because every swap requires a comparison first bu not every comparison requires a swap, so comparisons are a guaranteed repeated work 

# The outer loop as well as inner loop does n-1 work. For every outer loop pass the inner loop scans the list again so our work becomes (n-1) * (n-1) 
# And that inturn becomes (n-1)² and according to algebra when we expand on it with the rule (a-b)² = a² -2ab + b² it becomes (n-1)² = n² - 2n + 1

# In BigO notation we ask the question as input becomes huge with term dominates the growth and in our case of (n-1)² = n² - 2n + 1 . The n² dominates the growth as if the number n = 1,000,000 becomes n² = 1,000,000,000,000 the number -2n + 1 is tiny compared to that so we dont take that into consideration 

# Thus our Time complexity becomes O(n²) . First i will define what is quadratic, in maths quadratic means an polynomial equation or expression where the highest power of a variable is ² . In our case a quadratic time complexity means an algorithm whose execution time grows in proportion to the square of the input size.

# Thats why bubble sort is not used in massive data sets as work increases proportional to ² of input size 


# Bubble sort takes the additional space of O(1) because the extra additional memory used is only by our loop variables like _ & i and some temporary space used during comparison but the overall space complexity is O(n) because with increase in input the memory needed to store that input also increases.


# Insertion sort 

# 1. Start from the second element in the list because the first element is already considered sorted
# 2. Pick out the current element we are at
# 3. Move backward through the sorted portion of the list
# 4. Keep checking elements until we find where the current element belongs
# 5. Insert the current element into its correct sorted position
# 6. Repeat steps 2 to 5 until the whole list is sorted

def insertion_sort(nums):
    nums = list(nums)
    for i in range(1, len(nums)): # iterate the whole list and we start from index 1 because in insertion sort first element is already considered sorted
        cur = nums.pop(i) # we pop out the current element that we want to insert into the sorted portion i.e the starting left of the list. 
        j = i -1 # start checking from the element just before the current position
        while j >= 0 and nums[j] > cur: # To move left while elements are greater than current element
            j = j-1 # keep moving backward through the sorted portion
        nums.insert(j+1,cur)  # insert current element into its correct sorted position
    return nums

nums0, output0 = test0['input']['nums'], test0['output']

print('Input:', nums0)
print('Expected output:', output0)
result0 = insertion_sort(nums0)
print('Actual output:', result0)
print('Match:', result0 == output0)

print('\n')

nums = [5,2,1,4,0,3]
print(insertion_sort(nums))
print('\n')

results_insertion_sort = evaluate_test_cases(insertion_sort,tests[:6]) 

print('-------------------------------------')
print('\n')


# Complexity of Insertion sort 

# Insertion sort mainly does 3 main operations
# 1. comparison   2. backward traversal/searching   3. insertion

# The main idea behind insertion sort is that we treat the left side of the list as already sorted.
# We pick one element at a time from the unsorted portion and insert it into its correct position in the sorted portion.

# To analyze the time complexity we mainly focus on comparisons and backward traversal because every element may need to move backward through the sorted portion before being inserted.

# The outer loop runs n-1 times because we start from index 1 and assume the first element is already sorted.

# The while loop is where the main work happens.In the best case scenario like [1,2,3,4,5] the current element is already greater than elements before it.So the while loop stops immediately every time.
# This means only one comparison happens per iteration.Thus in the best case the total work grows linearly with input size.Therefore Best Case Time Complexity = O(n)

# In the worst case scenario like [5,4,3,2,1] every new element has to travel all the way left through the sorted portion.

# Example:
# 4 compares with 5
# 3 compares with 5 and 4
# 2 compares with 5,4 and 3

# This approximately grows like n². Thus Worst Case Time Complexity = O(n²). Average case is also O(n²) because for random lists elements usually move backward partially through the sorted portion.

# Even though insertion sort also has quadratic complexity like bubble sort,it is usually much faster in practice because instead of repeatedly swapping neighboring elements,it directly finds the correct position and inserts the element there.

# Bubble sort slowly moves elements one swap at a time. Insertion sort places elements more intelligently.

# Insertion sort takes additional space of O(1) because the extra memory used is only by helper variables like i, j and cur.

# But overall space complexity is O(n) because memory is still needed to store the input list itself as input size increases.






