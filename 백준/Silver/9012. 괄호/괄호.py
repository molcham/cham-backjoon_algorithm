import sys

T = int(sys.stdin.readline().strip())

for _ in range(T):
    ps = sys.stdin.readline().strip()
    stack = []
    for i in ps:
        if i == '(':
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                stack.append(i)
                break

    if len(stack):
        print('NO')
    else:
        print('YES')
