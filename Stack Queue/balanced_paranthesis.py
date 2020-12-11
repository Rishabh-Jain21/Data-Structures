from stack import Stack

'''
Here only paranthesis are given .No words or spaces 
'''


def balance_check2(s):
    stack = Stack()
    opening = set('([{')

    matches = set([('(', ')'), ('{', '}'), ('[', ']')])

    for paren in s:
        if paren in opening:
            stack.push(paren)
        else:
            if stack.size == 0:
                return False
            last_open = stack.pop()
            if(last_open, paren) not in matches:
                return False
    return stack.isEmpty()


def balance_check(s):
    if len(s) % 2 != 0:
        return False

    opening = set('([{')

    matches = set([('(', ')'), ('{', '}'), ('[', ']')])
    stack = []

    for paren in s:
        if paren in opening:
            stack.append(paren)
        else:
            if(len(stack) == 0):
                return False
            last_open = stack.pop()

            if(last_open, paren) not in matches:
                return False

    return len(stack) == 0


print(balance_check('[]{{}}'))
