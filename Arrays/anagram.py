"""
Check if two strings are anagrams or not
"""
def anagram(a, b):
    """
    Count the occurance of each letter in both word and check if equal or not
    Time complexity O(n^2)
    """
    
    for i in a:
        if i.isalnum():
            if a.count(i) == b.count(i):
                continue
            else:
                return False
    return True


def anagram2(a, b):
    """
    Sort the strings and compare them.
    Time complexity is O(nlogn) depends on sorting algorithm used
    """
    a = a.replace(" ", '').lower()
    b = b.replace(" ", '').lower()
    return(sorted(a) == sorted(b))


def anagram3(a, b):
    """
    Using a dictionary to maintain frequency count of each letter.
    decrementing frequency of each letter for second word and checking if any letter count is non zero
    """
    a = a.replace(" ", '').lower()
    b = b.replace(" ", '').lower()
    if(len(a) != len(b)):
        return False

    count = {}

    for letter in a:
        count[letter] = count.get(letter, 0)+1

    for letter in b:
        if letter in count:
            count[letter] -= 1
        else:
            return False

    for k in count:
        if count[k] != 0:
            return False
    return True

print(anagram(' 1124abac'.lower(), 'ca  4 2 11  ab'.lower()))
print(anagram2(' 1124abac'.lower(), 'ca  4 2 11  ab'.lower()))
print(anagram3(' 1124abac'.lower(), 'ca  4 2 11  ab'.lower()))
