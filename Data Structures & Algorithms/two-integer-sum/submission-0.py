class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = {}
        for i in range(len(nums)):
            if sums.get(target-nums[i], -1) != -1:
                return [sums[target-nums[i]], i]
            else:
                sums[nums[i]] = i