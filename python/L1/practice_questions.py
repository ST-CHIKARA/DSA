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