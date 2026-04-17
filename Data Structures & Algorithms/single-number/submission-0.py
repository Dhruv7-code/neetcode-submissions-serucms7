class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        if len(nums) == 0 or len(nums) > 30000:
            return 0
        
        indxs = {}

        for num in nums:
            indxs[num] = indxs.get(num,0)+1

        return min(indxs, key=indxs.get)