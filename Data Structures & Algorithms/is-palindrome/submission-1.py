class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = ''.join(c.lower() for c in s if c.isalnum())
        start = 0
        end = len(t)-1

        while start<end:
            if t[start] == t[end]:
                start += 1
                end -= 1
            else:
                return False
        return True
        