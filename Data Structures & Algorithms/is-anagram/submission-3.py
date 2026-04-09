class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        start = 0
        end = len(s)-1

        stack = []
        values = {}

        for i in s:
            values[i] = i

            if i in t and values[i]:
                pass
               
            else: 
                stack.append(i)

        if len(stack) == 0:
            return True

        else:
            return False
            
