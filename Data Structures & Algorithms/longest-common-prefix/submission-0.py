class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # veritcal scanning
        # for each char in arbitrary first string
        # compare with every corresponding char in other strings
        # if length of other string is equal to i, return res
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return s[:i]

        return strs[0]