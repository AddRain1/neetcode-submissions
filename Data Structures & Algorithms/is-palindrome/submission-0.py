class Solution:
    def isPalindrome(self, s: str) -> bool:
        s= s.replace(" ","").lower()
        s = [char for char in s if char.isalnum()]
        # set up two pointers, one at the front and back, and move them inwards
        j = len(s) - 1
        for i in range(len(s)//2):
            if s[i] != s[j]:
                return False
            j -= 1
        return True
