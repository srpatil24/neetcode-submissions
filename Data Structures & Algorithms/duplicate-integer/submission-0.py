class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # create empty set to track previously appeared values
        hasAppeared = set()
        for i in nums:
            if i in hasAppeared:
                return True
            hasAppeared.add(i)
        return False
        