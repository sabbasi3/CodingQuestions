
def minwindow(s,t):

    if len(t) > len(s) or not t:
        return ""

    tchar = {}
    for char in t:
        tchar[char] = tchar.get(char,0) + 1
    
    l = 0 

    schar = {}
    minlen = 0 
    minstrlen = float("inf")
    minstr = ""

    for r in range(len(s)):
        # first check if we have a success of all the characters of t
        if tchar in schar:
            if minlen < minstrlen: 
                minstrlen = minlen
                minstr =  s[l:r+1]

            l += 1

        
        if s[r] in tchar or minlen < minstrlen:
            schar[s[r]] = schar.get(s[char]) + 1
            minlen += 1
        else: 
            schar[s[l]] -= 1
            left += 1

    return minstr


s = "xyaz"
t = "yz"

ans = minwindow(s,t)

print(ans)




