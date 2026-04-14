class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s)>200000:
            return False

        converted_txt = list(map(str.lower, filter(str.isalnum, s)))
        start = 0
        non_match=0
        end = len(converted_txt)-1
        while start < end:
            if converted_txt[start] != converted_txt[end]:
                non_match += 1
            start += 1
            end -= 1
        
        if non_match == 0 :
            return True
        else:
            return False