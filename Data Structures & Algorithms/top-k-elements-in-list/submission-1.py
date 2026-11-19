class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = defaultdict(int)
        for i in nums:
            hash[i]+=1
        
        return sorted(hash, key=hash.get, reverse=True)[0:k]