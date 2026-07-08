class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        start = 0
        end = len(nums)-1

        while start<end:
            sum = nums[start] + nums[end]
            if sum>target:
                end -= 1
            elif sum<target:
                start += 1
            else:
                return [start,end]
        