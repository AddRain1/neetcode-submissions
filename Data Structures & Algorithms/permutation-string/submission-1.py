class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1 = {}
        freq2 = {}

        if len(s1) > len(s2):
            return False

        for c in s1:
            freq1[c] = 1 + freq1.get(c, 0)

        for i in range(len(s1)):
            freq2[s2[i]] = 1 + freq2.get(s2[i], 0)

        if freq1 == freq2:
            return True
        
        l = 0
        for r in range (len(s1), len(s2)):
            if freq2[s2[l]] == 1:
                del freq2[s2[l]] 
            else:
                freq2[s2[l]] -= 1
            l += 1 
    
            freq2[s2[r]] = 1 + freq2.get(s2[r], 0)

            if freq1 == freq2:
                return True
        
        return False

            
            
