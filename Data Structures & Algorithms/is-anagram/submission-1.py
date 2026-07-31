class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if lengths are different, return false
        if len(s) != len(t):
            return False

        # Loop through each char and put it's frequency in a dictionary
        freq_s = {}
        freq_t = {}

        for char in s:
            freq_s[char] = freq_s.get(char, 0) + 1
        
        for char in t:
            freq_t[char] = freq_t.get(char, 0) + 1

        return freq_s == freq_t