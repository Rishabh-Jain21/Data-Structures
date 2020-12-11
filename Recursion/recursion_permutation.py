import time


def permutate(s):
    out = []

    if(len(s) == 1):
        out = [s]
    else:
        for i, let in enumerate(s):
            # print(s[:i]+s[i+1:])
            for perm in permutate(s[:i]+s[i+1:]):
                out += [let+perm]
                #print(f'OUT {out}')
    return out


c1 = time.time()
print(len(permutate('abcdefghi')))
print(time.time()-c1)
