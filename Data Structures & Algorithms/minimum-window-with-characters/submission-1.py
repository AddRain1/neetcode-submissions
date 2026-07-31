class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tfreq = {}
        for c in t:
            tfreq[c] = 1 + tfreq.get(c, 0)
        freq = {}
        # start l pointer at 0
        l = 0
        # let r increment through whole string
        met = 0
        res, resLen = [-1, -1], float("infinity")
        for r in range(len(s)):
            freq[s[r]] = 1 + freq.get(s[r], 0)
            
            if s[r] in tfreq and freq[s[r]] == tfreq[s[r]]:
                met += 1
            
            while met == len(tfreq):
                if (r - l + 1) < resLen:
                    res = [l ,r]
                    resLen = r - l + 1
                freq[s[l]] -= 1
                if s[l] in tfreq and freq[s[l]] < tfreq[s[l]]:
                    met -= 1
                l+=1
        
        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""

        # move r pointer until frequency of letters in t match freq of s
        # shrink window while the frequencies are still valid
        # return every char in window