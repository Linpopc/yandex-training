def isValid(s):
    d = {
        '(': ')',
        '{': '}',
        '[': ']'
    }
    stack = []
    for i in s:
        if i in d:
            stack.append(i)
        elif len(stack) == 0 or i != d[stack.pop()]:
            return 'no'
    return 'yes' if len(stack) == 0 else 'no'

s = str(input())
res = isValid(s)
print(res)
