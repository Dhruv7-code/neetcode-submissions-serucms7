class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        if len(nums) == 1:
            return nums

        res = {}

        for i,a in enumerate(nums):
             res[a] = 1 + res.get(a,0)
        
        top_k = heapq.nlargest(k, res, key=res.get)

        return top_k