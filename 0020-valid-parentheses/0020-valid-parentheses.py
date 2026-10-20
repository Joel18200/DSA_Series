class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        pairs={')':'(',']':'[','}':'{'}
        for symbol in s:
            if symbol in pairs:
                if not stack or stack.pop()!=pairs[symbol]:
                    return False
            else:
                stack.append(symbol)
        return len(stack)==0                
        