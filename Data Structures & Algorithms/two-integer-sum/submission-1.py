class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = {}
        for i in range(len(nums)):
            curr = numDict.get(target-nums[i], -1)
            if curr == -1:
                numDict[nums[i]] = i
            else:
                return [numDict[target-nums[i]], i]