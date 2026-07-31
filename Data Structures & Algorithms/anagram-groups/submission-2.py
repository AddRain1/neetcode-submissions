from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # go through each string
        # for each 
        # use defaultdict
        map = defaultdict(list)
        for s in strs:
            sorted_s = "".join(sorted(s))
            map[sorted_s].append(s)
        return list(map.values())

