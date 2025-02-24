
class Solution:
    def encode(self, strs: list[str]) -> str:
        newstring = ""
        for word in strs:
            newstring += str(len(word)) + "/"  + word

        return newstring
    def decode(self, s: str) -> list[str]:
        res, i = [], 0 

        while i < len(s):
            j = i # use j to find the length of the word
            while s[j] != "/":
                j += 1
                
            length = int(s[i:j])

            word = s[j+1 : length + 1+ j]
            res.append(word)

            i = length + 1 + j ### update starting point of i instead of modifying string. # s = s[length + 1 + j:] # remove word from s string

        return res
    
    
sol = Solution()
encoded = sol.encode([ "neet", "code", "love", "you" ]) 
print(encoded)
decoded = sol.decode(encoded)
print(decoded)
# [ "neet", "code", "love", "you" ]
