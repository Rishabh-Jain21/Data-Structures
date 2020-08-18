def anagram(a, b):
    for i in a:
        if i.isalnum():
            if a.count(i) == b.count(i):
                continue
            else:
                return False
    return True


def anagram2(a, b):
    a = a.replace(" ", '').lower()
    b = b.replace(" ", '').lower()
    return(sorted(a) == sorted(b))


def anagram3(a, b):
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
            count[letter] = 1

    for k in count:
        if count[k] != 0:
            return False
    return True


print(anagram3(' 1124abac'.lower(), 'ca  4 2 11  ab'.lower()))
