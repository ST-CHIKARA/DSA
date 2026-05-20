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



# Ok now we move towards rectifying the inefficiencies we saw in bubble sort of it being O(n²)

# we will try to apply the right technique to rectify the inefficiencies 

# To perform sorting more efficiently we'll apply a strategy called divide and conquer which have the following general steps

# 1. Divide the input in roughly two equal parts
# 2. recursively solve the problem individually for each of the two parts 
# 3. Combine the results to solve the problem for the original inputs 
# 4. Include terminating conditions for small or indivisible inputs

# The name for this solution algo is Merge sort 

# Now we will come up with a solution and state it in plain english 

# 1. If the input list is empty or contains just one element it is already sorted, return it 
# 2. If not divide the list of numbers in roughly 2 equal parts
# 3. Sort each part recursively using merge sort algorithm and we get back 2 sorted lists
# 4. Merge the 2 sorted list to get a single sorted list


def merge(left, right):

    merged = []  # empty list to store the final sorted list

    i = 0  # pointer/counter for left list
    j = 0  # pointer/counter for right list

    # compare elements from both lists until one list finishes/ until elements still remain in the list. Even if elements gets exhausted in one list this statement becomes False
    while i < len(left) and j < len(right):

        # if current element in left list is smaller
        if left[i] <= right[j]: # We do this because logic says if 2 lists are already sorted so the smallest element remaining is definitely on the 0 position of i and if this condition gets satisfied 

            merged.append(left[i])  # we add it to empty merged list
            i += 1  # move left pointer/counter forward from 0 to 1 and we repeat the loop with the next value that counter points to 

        else:
            # If the if block dont run what we do is we take smallest element of the right sorted list and append it to the merged final list as that is the smallest element in this case 
            merged.append(right[j])  # add the smaller right element
            j += 1  # move right pointer/counter forward
    # Eventually a list gets exhausted and the upper while loop gets False so thats why to add the remaining elements we make another while loop
    # add remaining elements from left list if any are left
    while i < len(left):

        merged.append(left[i])
        i += 1

    # add remaining elements from right list if any are left
    while j < len(right):

        merged.append(right[j])
        j += 1

    return merged

def merge_sort(nums):

    # if list has 0 or 1 element it is already sorted
    if len(nums) <= 1: # Base case
        return nums

    # find the middle index to divide the list into 2 halves
    mid = len(nums) // 2

    # divide the left half of the list
    left = nums[:mid]

    # divide the right half of the list
    right = nums[mid:]

    # recursively sort both halves using merge sort
    left_sorted, right_sorted = merge_sort(left), merge_sort(right)

    # merge the two sorted halves into one sorted list
    sorted_nums = merge(left_sorted, right_sorted)

    # return the final merged sorted list
    return sorted_nums   


print(merge([1, 4, 7, 9, 11], [-1, 0, 2, 3, 8, 12]))
print()

nums0, output0 = test0['input']['nums'], test0['output']

print('Input:', nums0)
print('Expected output:', output0)
result0 = merge_sort(nums0)
print('Actual output:', result0)
print('Match:', result0 == output0)

print('----------------------------')
print('\n')


result_merges_sort = evaluate_test_cases(merge_sort,tests[:6])

print('\n')



# To analyze the complexity of merge sort we will add some scaffolding to the code of both merge and merge sort

# def merge(nums1, nums2, depth=0):
#     print('  '*depth, 'merge:', nums1, nums2)
#     i, j, merged = 0, 0, []
#     while i < len(nums1) and j < len(nums2):
#         if nums1[i] <= nums2[j]:
#             merged.append(nums1[i])
#             i += 1
#         else:
#             merged.append(nums2[j])
#             j += 1
#     return merged + nums1[i:] + nums2[j:]
        
# def merge_sort(nums, depth=0):
#     print('  '*depth, 'merge_sort:', nums)
#     if len(nums) < 2: 
#         return nums
#     mid = len(nums) // 2
#     return merge(merge_sort(nums[:mid], depth+1), merge_sort(nums[mid:], depth+1), depth+1)

# print(merge_sort([5, -12, 2, 6, 1, 23, 7, 7, -12]))

# print('\n')

# Another attempt at a better scaffolding 

def merge(nums1, nums2, depth=0):

    indent = "    " * depth

    print(f"{indent}MERGE")
    print(f"{indent}LEFT  : {nums1}")
    print(f"{indent}RIGHT : {nums2}")

    merged = []

    i, j = 0, 0

    while i < len(nums1) and j < len(nums2):

        print(f"{indent}COMPARE -> {nums1[i]} vs {nums2[j]}")

        if nums1[i] <= nums2[j]:

            print(f"{indent}TAKE LEFT  -> {nums1[i]}")

            merged.append(nums1[i])

            i += 1

        else:

            print(f"{indent}TAKE RIGHT -> {nums2[j]}")

            merged.append(nums2[j])

            j += 1

        print(f"{indent}MERGED NOW -> {merged}")
        print()

    if i < len(nums1):

        print(f"{indent}LEFT REMAINING  -> {nums1[i:]}")

    if j < len(nums2):

        print(f"{indent}RIGHT REMAINING -> {nums2[j:]}")

    result = merged + nums1[i:] + nums2[j:]

    print(f"{indent}MERGE RESULT -> {result}")
    print()

    return result


def merge_sort(nums, depth=0):

    indent = "    " * depth

    print(f"{indent}MERGE_SORT -> {nums}")

    if len(nums) <= 1:

        print(f"{indent}BASE CASE  -> {nums}")
        print()

        return nums

    mid = len(nums) // 2

    left = nums[:mid]
    right = nums[mid:]

    print(f"{indent}SPLIT")
    print(f"{indent}LEFT  : {left}")
    print(f"{indent}RIGHT : {right}")
    print()

    left_sorted = merge_sort(left, depth + 1)

    right_sorted = merge_sort(right, depth + 1)

    print(f"{indent}MERGING SORTED HALVES")
    print(f"{indent}LEFT SORTED  : {left_sorted}")
    print(f"{indent}RIGHT SORTED : {right_sorted}")
    print()

    return merge(left_sorted, right_sorted, depth + 1)


print()
print("FINAL RESULT ->", merge_sort([5, -12, 2, 6, 1, 23, 7, 7, -12]))
print()




# In merge sort the main operation responsible for most of the work is the merge operation.The splitting itself is cheap because we are mainly just dividing the list into smaller parts.The actual sorting happens during merging where elements are compared and combined into a new sorted list.

# The merge function works on two already sorted lists.During merging we repeatedly compare the current elements of both lists, append the smaller one into a new merged list and move the corresponding pointer forward.

# Since each element is processed only once during merging, if the total number of elements in both lists is n,then the merge operation takes O(n) time.

# Merge sort follows the divide and conquer strategy. It repeatedly divides the original list into two halves recursively until we reach lists of size 1. Lists of size 1 are automatically sorted and become the base case of recursion.

# The recursive splitting creates a tree like structure.

# Example:
# Level 0 -> 1 list of size n
# Level 1 -> 2 lists of size n/2
# Level 2 -> 4 lists of size n/4
# Level 3 -> 8 lists of size n/8

# Even though the number of lists increases at every level,
# the total amount of data across that entire level always remains n.

# Example:
# 2 * (n/2) = n
# 4 * (n/4) = n
# 8 * (n/8) = n

# So the total merge work done at every level of the recursion tree is O(n).

# Now we calculate how many levels exist in the recursion tree.
# At every level the list size keeps getting divided by 2.

# n -> n/2 -> n/4 -> n/8 -> ... -> 1

# The number of times we can divide n by 2 before reaching 1 is log₂(n). Therefore the recursion tree has log(n) levels.

# Since: Every level does O(n) work and there are O(log n) levels

# Total Time Complexity:
# O(n * log n)

# Therefore merge sort has:
# Best Case Time Complexity    = O(n log n)
# Average Case Time Complexity = O(n log n)
# Worst Case Time Complexity   = O(n log n)

# Unlike bubble sort and insertion sort, merge sort performs efficiently even for very large datasets because its growth rate is much slower than quadratic complexity.

# Space Complexity

# Merge sort creates new lists during the merge process. Inside merge() we create a new merged list where sorted elements are stored.

# Because additional arrays are created during merging, merge sort is not an in-place sorting algorithm like bubble sort or insertion sort.

# At first glance it may seem that every recursion level requires O(n) space, which may look like O(n log n) space overall.

# However after a merge operation finishes, older smaller sublists are no longer needed and their memory can be reused or discarded.

# Therefore the maximum additional memory used at any point remains proportional to n. Thus Additional Space Complexity = O(n)

# Merge sort basically trades additional memory usage for significantly faster sorting performance.



# Now after seeing how merge sort works and the inefficiencies it has that requires it to allocate additional space as large as the input itself. That makes it somewhat slow in practice because memory allocation is far more expensive than comparisons or swapping. So to overcome that we apply a new algo called quick sort.

# Quick sort

# Basically it works like this :-

# 1. If the list is empty or has just one element return it because the list is already sorted

# 2. Pick a random element from the list this is called a pivot

# 3. Reorder the list so that all elements with values less than or equal to the pivot comes before the pivot, while all elements with value greater than the pivot comes after it. This is called partitioning 

# 4. The pivot element divides the array into 2 parts which can be sorted independently by making a recursive call to quicksort.

def partition(nums, start=0, end=None):
    if end is None:
        end = len(nums) - 1

    pivot = nums[end]
    l, r = start, end - 1

    while l <= r:
        while l <= r and nums[l] <= pivot:
            l += 1

        while l <= r and nums[r] > pivot:
            r -= 1

        if l < r:
            nums[l], nums[r] = nums[r], nums[l]

    nums[l], nums[end] = nums[end], nums[l]
    return l

def quicksort(nums, start=0, end=None):
    if end is None:
        end = len(nums) - 1

    if start < end:
        pivot = partition(nums, start, end)
        quicksort(nums, start, pivot - 1)
        quicksort(nums, pivot + 1, end)

    return nums

l1 = [1, 5, 6, 2, 0, 11, 3]
pivot = partition(l1)
print(l1, pivot)
print()


nums0, output0 = test0['input']['nums'], test0['output']

print('Input:', nums0)
print('Expected output:', output0)
result0 = quicksort(nums0)
print('Actual output:', result0)
print('Match:', result0 == output0)
print('\n')


result_quicksort = evaluate_test_cases(quicksort,tests[:6])
print('\n')


# Analyzing the complexity

# In quicksort the main operation responsible for most of the work is the partition operation. During partitioning we rearrange elements around a pivot element so that: all elements smaller than or equal to the pivot move to the left side and all elements greater than the pivot move to the right side.

# The partition function mainly performs:
# 1. comparisons
# 2. pointer movement
# 3. swaps

# During one partition operation each element is usually visited once by either the left or right pointer. Therefore partitioning a list of size n takes O(n) time.

# After partitioning: the pivot reaches its final correct sorted position.
# Then quicksort recursively sorts: the left side of the pivot and the right side of the pivot

# Best Case / Average Case :- The best and average case happen when the pivot divides the list into two nearly equal halves.


# Similar to merge sort,the recursive partitioning creates a tree like structure. Even though the number of sublists increases at every level, the total amount of data processed across that level still remains n.



# Since partitioning each level together costs O(n), the total work done at every level of the recursion tree is O(n).

# At every level the list size keeps getting divided roughly by 2.

# n -> n/2 -> n/4 -> n/8 -> ... -> 1

# The number of times we can divide n by 2 before reaching 1 is log₂(n). Therefore the recursion tree has O(log n) levels.

# Since: Every level does O(n) work and there are O(log n) levels

# Total Time Complexity: O(n * log n)

# Therefore quicksort has:
# Best Case Time Complexity    = O(n log n)
# Average Case Time Complexity = O(n log n)


# Worst Case Complexity

# The worst case happens when the pivot repeatedly becomes the smallest or largest element.

# Example: [1,2,3,4,5] if the last element is always chosen as pivot. Partitioning becomes extremely unbalanced. Instead of dividing into: n/2 and n/2. We get: n-1 and 0 Then: n-2 and 0. Then: n-3 and 0

# This creates a deep recursive chain instead of a balanced recursion tree.Total comparisons become: n + (n-1) + (n-2) + ... + 2 + 1. Using arithmetic series: = n * (n-1) / 2. Which approximately grows like n². Therefore: Worst Case Time Complexity = O(n²)



# Space Complexity

# Unlike merge sort, quicksort does not create large extra merged arrays. Partitioning mostly happens inside the same original list by swapping elements. Therefore quicksort is considered an in-place sorting algorithm.

# The partition process itself only uses a few helper variables like: left pointer, right pointer, pivot position

# So the additional working memory used during partitioning is O(1). However recursive function calls still use stack memory.

# In the average case: recursion depth becomes O(log n)

# In the worst case:recursion depth becomes O(n)

# Therefore:
# Average Case Space Complexity = O(log n)
# Worst Case Space Complexity   = O(n)

# Quicksort basically trades the guaranteed stability of merge sort for faster practical performance and lower memory usage.




# Lets come back to our original question 

# Q. You're working on a new feature on Jovian called "Top Notebooks of the Week". Write a function to sort a list of notebooks in decreasing order of likes. Keep in mind that up to millions of notebooks can be created every week, so your function needs to be as efficient as possible.

# Here we need to we need to sort objects, not just numbers. Also, we want to sort them in the descending order of likes. To achieve this, all we need is a custom comparison function to compare two notebooks.


class Notebook:
    def __init__(self, title, username, likes):
        self.title, self.username, self.likes = title, username, likes
        
    def __repr__(self):
        return f'Notebook <"{self.username}/{self.title}", {self.likes} likes>'

    def __str__(self):
        return f'"{self.title}" by @{self.username} ({self.likes} likes)'


nb0 = Notebook('pytorch-basics', 'aakashns', 373)
nb1 = Notebook('linear-regression', 'siddhant', 532)
nb2 = Notebook('logistic-regression', 'vikas', 31)
nb3 = Notebook('feedforward-nn', 'sonaksh', 94)
nb4 = Notebook('cifar10-cnn', 'biraj', 2)
nb5 = Notebook('cifar10-resnet', 'tanya', 29)
nb6 = Notebook('anime-gans', 'hemanth', 80)
nb7 = Notebook('python-fundamentals', 'vishal', 136)
nb8 = Notebook('python-functions', 'aakashns', 74)
nb9 = Notebook('python-numpy', 'siddhant', 92)


notebooks = [nb0, nb1, nb2, nb3, nb4, nb5,nb6, nb7, nb8, nb9]


def compare_likes(nb1, nb2):
    if nb1.likes > nb2.likes:
        return 'lesser'
    elif nb1.likes == nb2.likes:
        return 'equal'
    elif nb1.likes < nb2.likes:
        return 'greater' 
    
def default_compare(x, y):
    if x < y:
        return 'less'
    elif x == y:
        return 'equal'
    else:
        return 'greater'

def merge_sort(objs, compare=default_compare):
    if len(objs) < 2:
        return objs
    mid = len(objs) // 2
    return merge(merge_sort(objs[:mid], compare), 
                 merge_sort(objs[mid:], compare), 
                 compare)

def merge(left, right, compare):
    i, j, merged = 0, 0, []
    while i < len(left) and j < len(right):
        result = compare(left[i], right[j])
        if result == 'lesser' or result == 'equal':
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    return merged + left[i:] + right[j:]


sorted_notebooks = merge_sort(notebooks, compare_likes)

print(sorted_notebooks)
print('\n')