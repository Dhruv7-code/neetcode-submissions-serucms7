class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False

        counter = 0
        for i in range(len(s)):
            if s.count(s[i]) != t.count(s[i]):
                return False
        return True