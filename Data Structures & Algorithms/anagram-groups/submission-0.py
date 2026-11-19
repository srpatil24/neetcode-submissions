class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lst = []
        seen = {}
        for i in strs:
            curr = "".join(sorted(i))
            val = seen.get(curr, -1)
            if val == -1:
                seen[curr] = len(lst)
                lst.append([i])
            else:
                lst[val].append(i)
        return lst