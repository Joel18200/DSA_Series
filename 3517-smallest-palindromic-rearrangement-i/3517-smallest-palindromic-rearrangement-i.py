class Solution:
    def smallestPalindrome(self, s: str) -> str:
        mid=len(s)//2
        if len(s)%2==0:
            a="".join(sorted(s[:mid]))
            return a+a[::-1]
        else:
            a="".join(sorted(s[:mid]))
            return a+s[mid]+a[::-1]
               

        