'''
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
'''



class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        slow = 1
        fast = 1

        while fast<len(nums):
            if nums[fast]!=nums[fast-1]:
                nums[slow] = nums[fast]
                slow+=1
            fast+=1
        return slow
        
