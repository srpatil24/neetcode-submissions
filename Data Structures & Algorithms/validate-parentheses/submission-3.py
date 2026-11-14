class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1: return False
        stack = []
        for i in s:
            match i:
                case '[' | '{' | '(':
                    stack.append(i)
                    continue
                case ']':
                    if not stack or stack[-1] != '[':
                        return False
                    stack.pop()
                case '}':
                    if not stack or stack[-1] != '{':
                        return False
                    stack.pop()
                case ')':
                    if not stack or stack[-1] != '(':
                        return False
                    stack.pop()
        return len(stack) == 0