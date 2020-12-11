def postfix(s):
    stack = []
    pos = ''
    prio = {"+": 1, "-": 1, "*": 2, "/": 2}
    for i in s:
        if i not in prio:
            pos = pos+i
        else:
            if not stack:
                stack.append(i)
            else:
                if(prio[i] > prio[stack[-1]]):
                    stack.append(i)
                else:
                    while(stack and (prio[i] <= prio[stack[-1]])):
                        pos = pos+stack.pop()
                    stack.append(i)
    while(stack):
        pos = pos+stack.pop()
    return pos

def evaluation(post):
    stack = []
    result = 0
    prio = {"+": 1, "-": 1, "*": 2, "/": 2}
    for i in post:
        if i not in prio:
            stack.append(int(i))
        else:
            b1 = stack.pop()
            a1 = stack.pop()
            if i == '+':
                result = a1+b1
            if i == '-':
                result = a1-b1
            if i == '*':
                result = b1*a1
            if i == '/':
                result = a1/b1
            stack.append(result)
    return stack[-1]


print(postfix('a+b*d'))
print(postfix('2*6/3'))
print(evaluation('42/'))
print(evaluation(postfix('2*6/3')))
