'''
Given string of words reverse all the words
eg:-
    This is the best.

return
    best the is This
'''


def rev_word(s):
    s = s.strip().split()
    s.sort(reverse=True)
    return(' '.join(s))


def rev_word1(s):
    return " ".join(reversed(s.strip().split()))


def rev_word2(s):
    return " ".join(s.split()[::-1])


def rev_word3(s):
    words = []
    length = len(s)
    space = [' ']
    i = 0
    while i < length:
        if s[i] not in space:
            word_start = i

            while i < length and s[i] not in space:
                i = i+1
            words.append(s[word_start:i])
        i = i+1
    return " ".join(reversed(words))


print(rev_word("   This is the    best    "))
