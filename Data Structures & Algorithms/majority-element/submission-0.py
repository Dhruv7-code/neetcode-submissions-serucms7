class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        app=len(nums)//2
        for i in set(nums):
            if nums.count(i)>app:
                return i