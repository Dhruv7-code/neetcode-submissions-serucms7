class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) > 10000:
            return False
        
        inds = {}
        for i, n in enumerate(nums):
            inds[n] = i
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in inds and inds[diff]!=i:
                return [i,inds[diff]]
        return []