# Example 
# s1 = "abc"
# s2 = "lecabee"
# 

def perm(s1,s2):

    window = len(s1)
    s1char = {}
    s2char = {}
    l = 0

    for char in s1:
        s1char[char] = s1char.get(char, 0)  + 1

    for char in s2: 
        s2char[char] = s2char.get(char, 0)  + 1

    # for r in range(len(s2)):
    #     if s2[r] in s1char: 
    #         s1char[s2[r]] = s1char.get(s2[r], 0) - 1
    #     else: 
    #         while l <= r:
    #             if s2[l] in s1char:
    #                 s1char[s2[l]] += 1
    #             l += 1
    #         l = r + 1

    #     if (r-l+1) > window:
    #         if s2[l] in s1char: 
    #             s1char[s2[l]] = s1char.get(char, 0) + 1
    #         l += 1

        
    #     if (r-l+1) == window:
    #         if all(value == 0 for value in s1char.values()):
    #             return True


    return False



ans = perm("abc", "lecabee")

print(ans)