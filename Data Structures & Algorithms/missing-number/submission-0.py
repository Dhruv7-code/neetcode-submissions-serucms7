class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        freq = {}

        for num in nums:
            freq[num] = 1
        
        for i in range(len(nums)+1):
            if i not in freq:
                return i
        