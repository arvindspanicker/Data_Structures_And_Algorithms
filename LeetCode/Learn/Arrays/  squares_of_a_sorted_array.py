"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?

 
"""


class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        # first find the first positive number
        first_non_neg_index = -1
        for index,item in enumerate(nums):
            if item>0:
                first_non_neg_index = index
                break
        
        negative_number_iterator = first_non_neg_index - 1 if first_non_neg_index >=0 else len(nums)-1 
        positive_number_iterator = first_non_neg_index if first_non_neg_index != -1 else len(nums) + 1 

        while negative_number_iterator >=0 and positive_number_iterator < len(nums):
            if abs(nums[negative_number_iterator]) >  abs(nums[positive_number_iterator]):
                result.append(nums[positive_number_iterator]**2)
                positive_number_iterator += 1
            else:
                result.append(nums[negative_number_iterator]**2)
                negative_number_iterator -= 1
        
        while negative_number_iterator >=0:
            result.append(nums[negative_number_iterator]**2)
            negative_number_iterator -= 1
        
        while positive_number_iterator < len(nums):
            result.append(nums[positive_number_iterator]**2)
            positive_number_iterator += 1

        return result



