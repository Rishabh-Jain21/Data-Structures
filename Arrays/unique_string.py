'''
abcde -> unique characters

aabcde -> not unique characetrs
'''


def unique(s):
    if len(s) != len(set(s)):
        return False
    return True


def unique2(s):
    chars = set()
    for let in s:
        if let in chars:
            return False
        else:
            chars.add(let)
    return True


print(unique2("abcdefgha"))
