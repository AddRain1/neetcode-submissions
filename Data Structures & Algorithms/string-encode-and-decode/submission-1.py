class Solution:

    def encode(self, strs: List[str]) -> str:
        # join every string in strs with a delimiter that contains the length of string and #
        return ''.join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        # to decode one string into a list of strings, we use two pointers
        result = []
        i = 0

        while i < len(s):

            j = i

            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])
            string = s[j+1 : j+1+length]

            result.append(string)

            i = j + 1 + length

        return result
