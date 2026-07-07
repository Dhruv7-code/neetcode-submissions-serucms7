class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sarr = []
        tarr = []
        for i in range(len(s)):
            sarr.append(s[i])
            tarr.append(t[i])
        sarr.sort()
        tarr.sort()
        return sarr==tarr