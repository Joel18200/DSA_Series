class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        pairs={')':'(',']':'[','}':'{'}
        for symbol in s:
            if symbol in '([{':
                stack.append(symbol)
            else:
                if not stack or stack[-1]!=pairs[symbol]:
                    return False
                stack.pop()
        return len(stack)==0                
        