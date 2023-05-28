'''
abcde -> unique characters

aabcde -> not unique characetrs
'''


def unique(s):
    """
    comparing length of set and length of string 
    """
    if len(s) != len(set(s)):
        return False
    return True


def unique2(s):
    """
    Adding not seen characters in a set and if a character is found in set we return false
    """
    chars = set()
    for let in s:
        if let in chars:
            return False
        else:
            chars.add(let)
    return True


print(unique2("abcdefgha"))
