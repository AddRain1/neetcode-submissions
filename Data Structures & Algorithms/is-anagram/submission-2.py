class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # freq of characters
        freq1 = dict()
        freq2 = dict()
        for char in s:
            freq1[char] = freq1.get(char, 0) + 1
        for char in t:
            freq2[char] = freq2.get(char, 0) + 1
        return freq1.items() == freq2.items()