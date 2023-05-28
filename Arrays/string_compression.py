'''
AABBCCC -> A2B2C3
AAABCCCCDDDD -> A3B1C4D4
AABAABC -> A2B1A2B1C1

'''



def compress(s):
    r = ''
    l = len(s)

    if l == 0:
        return ''
    if l == 1:
        return s+"1"

    last = s[0]
    cnt = 1
    i = 1
    while i < l:

        if(s[i] == s[i-1]):
            cnt += 1
        else:
            r = r+s[i-1]+str(cnt)
            cnt = 1
        i = i+1

    r = r+s[i-1]+str(cnt)

    return r

def compress_2(s):
    result=""
    i=0
    j=0
    n=len(s)
    while j<n:
        if s[i]==s[j]:
            j=j+1
        else:
            result=result+s[i]+str(j-i)
            i=j
    result=result+s[i]+str(j-i) # This is a case for last set of repeating characters
    return result

print(compress('AABAABC'))
print(compress_2('AABAABC'))

