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


a = []

result = 0


def permutate_2(output, string, result):
    if len(string) == 0:
        a.append(output)
        result = result+1
        return result

    for i in range(len(string)):
        op_1 = output+string[i]
        k = string[:i]+string[i+1:]
        return permutate_2(op_1, k, result)


print((permutate('abc')))
print(permutate_2("", 'abc', result))
print(a)
