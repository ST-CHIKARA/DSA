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
