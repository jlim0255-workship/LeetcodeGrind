"""
Twosum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

 

Constraints:

    2 <= nums.length <= 104
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    Only one valid answer exists.
"""
def twoSum(nums, target):
    # initialize a dict to hold {nums[i] : index of i} value pairs
    tbl = {}

    for i in range(len(nums)):
        #find the complement of i
        complement = target - nums[i]

        # if the complement is in dict, we get the complement index and return result
        if complement in tbl:
            return [i, tbl[complement]] # return index not value yaa
        
        # else, we store the value, index pair
        else:
            tbl[nums[i]] = i


if __name__ == "__main__":
    print(twoSum([2,7,11,15], 9))
