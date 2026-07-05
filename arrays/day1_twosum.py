#day 1: two sum 
#link: https://leetcode.com/problems/two-sum

def twoSum(self, nums, target):
        prevmap = {}

        for i , n in enumerate (nums):
            diff = target - n
            if diff in prevmap:
                return [prevmap[diff], i]
            prevmap[n] = i 


#beginner solution 
class Solution(object):

    def twoSum(self, nums, target):

        for i in range(len(nums)):

            for j in range(i + 1, len(nums)):

                if nums[i] + nums[j] == target:
                    return [i, j]
