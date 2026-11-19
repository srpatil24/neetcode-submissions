class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            srted = sorted(s)
            res[tuple(srted)].append(s)
        return list(res.values())