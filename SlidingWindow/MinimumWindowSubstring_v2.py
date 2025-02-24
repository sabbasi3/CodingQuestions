
def minwindow(s,t):

    if len(t) > len(s) or not t:
        return ""

    tchar = {}
    schar = {}
    for char in t:
        tchar[char] = tchar.get(char,0) + 1
    
    l = 0 

    minstrlen = float("inf")
    minstr = ""

    have, need = 0, len(tchar)

    for r in range(len(s)):

        if s[r] in tchar:
            schar[s[r]] = schar.get(s[r],0) + 1
            if schar[s[r]] == tchar[s[r]]:
                have += 1

        while have == need:
            if r - l + 1 < minstrlen:
                minstrlen = r - l + 1
                minstr = s[l:r+1]

            schar[s[l]] -= 1
            if s[l] in tchar and schar[s[l]] < tchar[s[l]]:
                have -= 1
            l += 1

    return minstr


s = "xyaz"
t = "yz"

ans = minwindow(s,t)

print(ans)




