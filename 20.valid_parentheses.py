class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        matches={
            ']':'[','}':'{',')':'('
        }
        for ch in s:
            if ch in matches.values():
                stack.append(ch)
            else:
                if not stack or stack[-1]!=matches[ch]:
                    return False
                else:
                    stack.pop()
        return len(stack)==0