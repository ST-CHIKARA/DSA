# Leet code

# (Q1-704) Binary search (Easy) # EXACT MATCH SEARCH 

# Given an array of int nums which is sorted in ascending order and an int target. Write a function to search target in nums. If target exists then return its index. Otherwise return -1

import time

tests0 = []

tests0.append({"input": {"nums": [-1, 0, 3, 5, 9, 12], "target": 9}, "output": 4})

tests0.append({"input": {"nums": [-1, 0, 3, 5, 9, 12], "target": 2}, "output": -1})


def evaluate_test_case(func, test, display=True):
    inputs = test["input"]
    expected = test["output"]

    start = time.time()
    actual = func(**inputs)
    end = time.time()

    exec_time = (end - start) * 1000

    passed = actual == expected

    if display:
        print("Input:", inputs)
        print("Expected output:", expected)
        print("Actual output:", actual)
        print("Execution time:", round(exec_time, 4), "ms")
        print("Test result:", "PASSED" if passed else "FAILED")
        print()

    return actual, passed, exec_time


def evaluate_test_cases(func, tests, display=True):
    total = len(tests)
    passed = 0
    failed = 0
    for i, test in enumerate(tests):
        print(f"Test case {i}")
        _, test_passed, _ = evaluate_test_case(func, test, display=display)
        if test_passed:
            passed += 1
        else:
            failed += 1
    print("SUMMARY")
    print(f"TOTAL:{total}, PASSED:{passed}, FAILED:{failed}")


def search_target(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        mid_number = nums[mid]
        if mid_number == target:
            return mid
        elif mid_number > target:
            hi = mid - 1
        else:
            lo = mid + 1
    return -1


print("--ANSWER 1--")
print()
evaluate_test_cases(search_target, tests0)
print()


print("---------")
print()


# (Q2-35) Search insert position (Easy) # BOUNDARY SEARCH (LOWER BOUND)

# Write a function given a sorted array/list of distinct integers and a target value, return the index if target is found and if not return the index where it would be if were to be inserted in order

tests1 = []

tests1.append({"input": {"nums": [1, 3, 5, 6], "target": 5}, "output": 2})

tests1.append({"input": {"nums": [1, 3, 5, 6], "target": 2}, "output": 1})

tests1.append({"input": {"nums": [1, 3, 5, 6], "target": 7}, "output": 4})

tests1.append({"input": {"nums": [1, 3, 5, 6], "target": 0}, "output": 0})


def search_insert(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        mid_number = nums[mid]
        if mid_number == target:
            return mid
        elif mid_number > target:
            hi = mid - 1
        else:
            lo = mid + 1
    return lo  # we are returning lo here because lo is the position that the target is supposed to be if inserted in the order


print("--ANSWER 2--")
print()
evaluate_test_cases(search_insert, tests1)
print()



# (Q3-34) Find first and last position of element in sorted array 

# Given an array of integers nums sorted in ascending order. find the start and ending position of a given number.

# This question differs from our exact match search because we are looking for both the start index and end index 

tests2 = []

tests2.append({
    'input':{
        'nums':[5,7,7,8,8,10],
        'target':8
    },
    'output':(3,4)  
})


tests2.append({
    'input':{
        'nums':[5,7,7,8,8,10],
        'target':6
    },
    'output':(-1,-1)   
})


tests2.append({
    'input':{
        'nums':[5,7,7,8,8,10],
        'target':0
    },
    'output':(-1,-1)   
})


# we will use generic binary search for our answer

def binary_search(lo,hi,condition):
    while lo<=hi:
        mid = (lo+hi) // 2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        else:
            lo = mid + 1
    return -1
        


def first_position(nums,target):
    def condition(mid):
        if nums[mid] == target:
            if mid > 0 and nums[mid-1] == target:
                return 'left'
            return 'found'
        elif nums[mid] < target:
            return 'right'
        else:
            return 'left'
    return binary_search(0, len(nums) - 1, condition)


def last_position(nums,target):
    def condition(mid):
        if nums[mid] == target:
            if mid < len(nums)-1 and nums[mid+1] == target:
                return 'right'
            return 'found'
        elif nums[mid] < target:
            return 'right'
        else:
            return 'left'
    return binary_search(0,len(nums)-1,condition)

def first_and_last_position(nums,target):
    return first_position(nums,target), last_position(nums,target)

print("--ANSWER 3--")
print()
evaluate_test_cases(first_and_last_position,tests2)
print()



# I will explain the data flow of how we reach our expected answer using our 1st test case of this question so test2[0] is:- 'nums':[5,7,7,8,8,10],'target':8 and expected 'output':(3,4)  

# this binary search will help us move around in our list to find our 1st occurrence and last occurrence of target

def binary_search(lo,hi,condition):
    while lo<=hi:
        mid = (lo+hi) // 2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        else:
            lo = mid + 1
    return -1

 # now comes the function that will help us find our first occurrence

def first_position(nums,target):
    def condition(mid): # condition func to get our found,right,left
        if nums[mid] == target: 
            if mid > 0 and nums[mid-1] == target:
                return 'left'
            return 'found'
        elif nums[mid] < target: 
            return 'right'
        else:
            return 'left'
        # after defining our condition we call binary_search and pass it into binary search below. what happening here is we are telling binary search to start from index 0 (lo) and till len(num) - 1 which is our (hi) and at every step it should use our condition function to come to a conclusion that is to go left right or found
    return binary_search(0, len(nums) - 1, condition)

# in our test case in 1st iteration lo = 0 and hi = 5 so mid becomes (0+5) //2 = 2 and now nums[2] is 7 so our condition elif nums[2] = 7 < target(8) becomes true and we get returned right and immediately or left side of the list got discarded. As we got right returned the algo checks what does right mean and binary search says if right is returned make lo = mid + 1 so that makes our lo = 2+1 = 3 so now in 2nd iteration our lo = 3 and hi = 5 that makes our mid (3+5) // 2 = 4 and nums[4] is 8, good we just found 8 but we have to check if its the 1st occurrence so firstly our data goes if nums[4] which is 8 == target(8) ok its true then we move in the condition nested below if mid > 0 its true and nums[mid-1] == target now nums[4-1=3] is also 8 this again is true and we get returned left now algo searches what to do with left and binary search says left means hi = mid - 1 and that makes our hi = 4-1=3 now comes the 3rd iteration our lo = 3 and hi = 3 that makes our mid = (3+3) //2 = 3 now nums[3] = 8 we again check if its == target, its true then we check if mid > 0  its true and nums[mid-1] = nums[3-1=2] == target(8) and at nums[2] is 7 so this becomes false and we get returned found and bingo we got our 1st occurrence of target which is 3


# now comes the function that helps us find last occurrence 

def last_position(nums,target):
    def condition(mid):
        if nums[mid] == target:
            if mid < len(nums)-1 and nums[mid+1] == target:
                return 'right'
            return 'found'
        elif nums[mid] < target:
            return 'right'
        else:
            return 'left'
    return binary_search(0,len(nums)-1,condition)

# in first iteration lo = 0 and hi = 5 , mid = (0+5)//2 = 2 , nums[2] = 7 we move right and lo becomes mid + 1 = 2+1=3 , now in 2nd iteration lo = 3,hi = 5, mid = (3+5)//2 = 4 , nums[4] = 8 we check if nums[4] == target(8) its true then we check if mid < len(nums)-1  so mid = 4 and len(num) = 6 - 1 = 5 so our condition becomes 4<5 = true and nums[mid+1] = nums[4+1=5] = 10 that becomes false and we get returned found and it returns mid position as the last occurrence which is 4

# and lastly we wrap the results of both the first occurrence and last occurrence in this def first_and_last_position(nums,target):return first_position(nums,target), last_position(nums,target) and it returns (return value of first_occurrence,last_occurrence) and then we check it against the expected output with the help of our evaluate_test_cases



# Assignment from the video

# Problem - Rotated lists

# You are given a list of numbers obtained by rotating a sorted list an unknown number of times. Write a function to determine the minimum number of times the original sorted list was rotated to obtain the given list. Your function should have the worst case complexity of O(log N) 
# The example is list [5,6,9,0,2,3,4] was obtained by rotating the sorted list [0,2,3,4,5,6,9] 3 times.
# we define 'rotating a list' as removing the last element of the list and adding it before the first element for example rotating the list [3,2,4,1] will produce [1,3,2,4]

# This question is similar in concept with leetcode problem (Q-153) which is find minimum in rotated sorted array 

# ANSWER

# Step 1 :- 

# Q:- State the Problem in simpler terms:-
# A:- Given a rotated sorted list that was rotated some unknown number of times we need to find the minimum number of times it was rotated to get our rotated list from the original list 

# Q:- The function you will write will take one input called nums. what does it represent give an answer
# A:- nums is a list that was originally sorted [3,5,6,7,9] but then rotated  [7,9,3,5,6]

# Q:- The function you write will return a single output called rotations. what does it represent 
# A:- rotations represent how many times a sorted list was rotated and in the example above the answer is 2 times because if the list was sorted initially it would look like [3,5,6,7,9] so if we rotate it one time it becomes [9,3,5,6,7] and one more time [7,9,3,5,6]. And in our (Q-153) rotation represents the index of minimum element in the array or we can return index at which the minimum element is present. another insight that we can get from this is:- number of rotations = index of the minimum element  


# Step 2 :-

# Now we will come up with some input and output examples and try to cover all edge cases 

tests3 = []

# Test case 0

# A list of size 10 rotated 3 times 

tests3.append({
    'input':{
        'nums':[19,25,29,3,5,6,7,9,11,14]
    },
    'output':3 # 3 is at index 3 = 3 rotations or we can just count 
})

# Test case 1

# A list of size 8 rotated 5 times 

tests3.append({
    'input':{
        'nums':[7,9,11,14,19,3,5,6]
    },
    'output':5 # number 3 at 5th index = 5 rotations
})

# Test case 2 

# A list that wasn't rotated at all 

tests3.append({
    'input':{
        'nums':[3,5,6,7,9,11,14]
    },
    'output':0 # no change in the list as it is fully sorted with no breakpoint (by breakpoint i mean where the sorted order breaks for eg if the list was [4,5,1,2,3] 4,5 are sorted in ascending order then immediately we see 1, it breaks the sorted order at index[2]) in ascending order so we need 0 rotations and 3 is also at index 0
})

# test case 3

# A list that was rotated just once

tests3.append({
    'input':{
        'nums':[14,3,5,6,7,9,11]
    },
    'output':1 # 3 at index 1 = 1 rotation 
})

# Test case 4

# A list that was rotated n-1 times where n is size of the list 

tests3.append({
    'input':{
        'nums':[5,6,7,9,11,14,19,25,29,3]
    },
    'output':9 # 3 at index 9 = 9 rotations 
})

# Test case 5 

# A list that was rotated n where n is size of the list 

tests3.append({
    'input':{
        'nums':[1,2,3,4,5]
    },
    'output':0 # no change in the list again as the sorted order is perfect and no break in the list and min element is also at index 0
})

# Test case 6

# List is empty

tests3.append({
    'input':{
        'nums':[]
    },
    'output':-1 # we dont have any element to access so we return -1
})

# Test case 7 

tests3.append({
    'input':{
        'nums':[3]
    },
    'output':0 # we only have 1 element so there is no list to be sorted and its the 0 index 
})

# Test case 8

# List of size 5 rotated 2 times

tests3.append({
    'input':{
        'nums':[4,5,1,2,3]
    },
    'output':2
})




# Step 3 :-

# Now we will come up with a solution to our problem and state it simply 

# To put it simply if we rotate a sorted list (x) times the smallest number in that list end up at position (x) eg:- [7,9,11,14,19,3,5,6] if we say this list was rotated 5 times then the smallest number should also be at index 5 and what is at index[5] ?, its 3 that's the smallest number in the list so this proves our theory and it is also the only number in the list that is smaller than the number before it, taking our example above 3 is smaller than 19 so this proves this theory too. so what we need to do is to check for each number in the list whether it is smaller than the number that comes before it(if there is a number before it) and the index at which that smaller number is present is our answer and if this condition dont come true that means there is no break in the sorted order and the list wasn't rotated at all.

# The above explanation is in the context of linear search 

# linear search solution 

# create a variable position with value = 0
# compare the number at current position with the number before it
# if the number is smaller than the number before it then return its position
# otherwise increment the position till we have exhausted all numbers 

def count_rotation_linear(nums):
    position = 0
    while position < len(nums): 
        if position > 0 and nums[position] < nums[position-1]: 
            return position
        position+=1
    if len(nums) == 0: # to handle the edge case where there is an empty list 
        return -1
    return 0 

print('----LINEAR SEARCH ANSWER----')
print()
evaluate_test_cases(count_rotation_linear,tests3)
print()


# but we have to solve this question using binary search so what will the understanding of binary search implementation be like ?

# Binary search solution

# define variables lo and hi for search space
# find the mid of the list 
# check if nums[mid] < nums[mid-1] if condition is true return the mid as the ans
# if not we need to decide which direction we need to go to search the answer because as we are using binary search and starting in the middle and mid is not the answer our answer may be on the right or left so to do that we need to compare nums[mid] with the nums[hi] and if nums[mid] is less than nums[hi] (nums[mid]<nums[hi]) and as our list is sorted, even with a break 2 halves are sorted it would mean that the right side of the list is perfectly sorted and there is no break on the right side and to put it simply numbers on right side of the the mid till hi are bigger than mid so as we are looking for the smallest number in the list right side dont have it so we just discard it and search in the left half of the list (hi = mid-1) and if our nums[mid] > nums[hi] it would mean as numbers are in sorted order and increase towards right side but here we have a number at nums[hi] which is smaller than the nums[mid] the break should have happened on the right side so the left side of the list dont contain a smaller and we have to move to the right side of the list to find our answer by (lo = mid+1)
# and if no break is found we just return 0 or -1 


def count_rotation_binary(nums):
    if len(nums) == 0: # guard clause that check for empty list
        return -1
    lo,hi=0,len(nums)-1
    while lo<=hi: 
        mid = (lo+hi)//2
        print('lo:',lo,',hi:',hi,',mid:',mid) # print debug
        if mid > 0 and nums[mid] < nums[mid-1]: # checking if mid is the ans
            return mid
        elif nums[mid] <= nums[hi]: # checking if ans is on the left side
            hi = mid - 1
        else:
            lo = mid + 1 # checking if ans on right side
    return 0 

print('----BINARY SEARCH ANSWER----')
print()
evaluate_test_cases(count_rotation_binary,tests3)
print()


# Answer using generic binary search 

def binary_search(lo,hi,condition):
    while lo<=hi:
        mid = (lo+hi) // 2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        else:
            lo = mid + 1
    return lo # we return lo because it is the only index at which minimum could be


def count_rotations_generic_binary(nums):
    if len(nums) == 0:
        return -1
    hi = len(nums)-1
    def condition(mid):
        if mid > 0 and nums[mid] < nums[mid-1]:
            return 'found'
        elif nums[mid] <= nums[hi]:
            return 'left'
        else:
            return 'right'
    return binary_search(0,len(nums)-1,condition)

print('----GENERIC BINARY SEARCH RESULTS----')
print()
evaluate_test_cases(count_rotations_generic_binary,tests3)
print()


# Answer for leetcode (Q-153)

tests4 = []

tests4.append({
    'input':{
        'nums':[3,4,5,1,2]
    },
    'output':1
})

tests4.append({
    'input':{
        'nums':[4,5,6,7,0,1,2]
    },
    'output':0
})

tests4.append({
    'input':{
        'nums':[11,13,15,17]
    },
    'output':11
})


def find_min(nums):
    lo,hi=0,len(nums)-1
    if len(nums) == 0:
        return -1
    while lo<=hi:
        mid = (lo+hi)//2
        print('lo:',lo,',hi:',hi,',mid:',mid)
        if mid > 0 and nums[mid] < nums[mid-1]:
            return nums[mid]
        elif nums[mid] <= nums[hi]:
            hi = mid - 1
        else:
            lo = mid + 1
    return nums[0]

print('----LEETCODE (Q-153) RESULTS----')
print()
evaluate_test_cases(find_min,tests4)
print()