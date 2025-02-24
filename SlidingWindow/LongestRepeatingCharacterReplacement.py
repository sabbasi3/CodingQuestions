# Example: s = "XYYY" k = 2
def charreplace(s, k):
    
    l = 0
    maxlen = 0
    count = {}

    for r in range(len(s)):
        count[s[r]] = count.get(s[r],0) + 1

        while (r-l+1) - max(count.values()) > k:
            count[s[l]] -= 1
            l+= 1

        maxlen = max(maxlen, (r-l + 1))

    return maxlen
    # l = 0 
    # maxlength = 0 
    # change = k 

    # charSet = set()

    # for r in range(1,len(s)):

    #     if s[r] not in charSet:
    #         change -= 1

    #     charSet.add(s[r])   
            
    #     maxlength = max(maxlength, r - l + 1)

    #     if change == 0:
    #         l += 1 
    #         change = k

    # return maxlength 

ans = charreplace("XYXY", 1)

print(ans)

ans = charreplace("XYYY", 2)

print(ans)