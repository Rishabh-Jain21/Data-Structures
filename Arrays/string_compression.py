'''
AABBCCC -> A2B2C3
AAABCCCCDDDD -> A3B1C4D4
'''


def compress(s):
    count = {}

    for char in s:
        count[char] = count.get(char, 0)+1

    result = ''
    for key, value in count.items():
        result += f'{key}{value}'

    return result


def compress2(s):
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


print(compress2('AAB'))
