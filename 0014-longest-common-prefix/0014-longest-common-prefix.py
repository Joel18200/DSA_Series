class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        s=min(strs,key=len)
        for i in range(len(s)):
            current_character=s[i]
            for word in strs:
                if current_character!=word[i]:
                    return s[:i]
        return s        
