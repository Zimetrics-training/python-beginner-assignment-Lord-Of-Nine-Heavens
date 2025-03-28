"""
Problem: Find the Longest Consecutive Sequence
Given an unsorted array of integers, write a function longest_consecutive(nums) 
that returns the length of the longest consecutive elements sequence.

Example: if nums = [100, 4, 200, 1, 3, 2]; The function should return 4, 
since the longest consecutive elements sequence is [1, 2, 3, 4].

Look for difference of 1 between two consecutive numbers.
"""
def longest_consecutive(nums):
    
    if not nums:
        return 0

    longest_streak = 1
    currstreak = 1
    nums.sort()

    for i, v in enumerate(nums[1:], start=1):
        if v == nums[i - 1]:  
            currstreak = 1

        elif v == nums[i - 1] + 1:
            currstreak += 1
        else:
            currstreak = 1

        longest_streak = max(longest_streak, currstreak)

    return longest_streak
