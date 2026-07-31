class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # creates a default dict
        res = defaultdict(list)

        # for every string in input list
        for s in strs:
            # sorted returns a new list, and ''.join turns it back into a string
            sortedS = ''.join(sorted(s))
            # append original string as one of the values of the sorted string key
            res[sortedS].append(s)
        
        return list(res.values())
        

