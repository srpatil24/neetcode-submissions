class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1: return False
        stck = []
        mp = {
            '}':'{',
            ']':'[',
            ')':'(',
        }
        for i in s:
            if i in mp:
                if len(stck) and stck[-1] == mp[i]:
                    stck.pop()
                    continue
                else:
                    return False
            stck.append(i)
        return False if len(stck) else True