class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1: return False
        stk = []
        mp = {
            '}':'{',
            ']':'[',
            ')':'(',
        }
        for i in s:
            if i in mp:
                if len(stk) and stk[-1] == mp[i]:
                    stk.pop()
                    continue
                else:
                    return False
            stk.append(i)
        return False if len(stk) else True