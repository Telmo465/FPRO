def palindrome_index(s):
    if s == s[::-1]:
        return -1
    for i in s:
        j = s.index(i)
        print (s[:j] ,s[j+1:] )
        st = s[:j] + s[j+1:]
        if st == st[::-1]:
            return j
    else:
        return -1
print(palindrome_index("aaaaab"))
