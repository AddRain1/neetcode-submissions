class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        substring = set()

        if len(s) < 1:
            return 0
        
        l, r = 0, 0
        while r < len(s):
            if s[r] not in substring:
                substring.add(s[r])
            else:
                while s[r] in s[l:r]:
                    substring.remove(s[l])
                    l+= 1   
                substring.add(s[r])
            maxLength = max(maxLength, r - l + 1)
            r+=1
        return maxLength
            
