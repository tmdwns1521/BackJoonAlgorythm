import sys

command = sys.stdin.readline().strip()
cnt = 0

stack = []
result = 0
for i in command:
    if "(" == i:
        cnt += 1
    if ")" == i:
        cnt -= 1
        if stack[-1] == "(":
            result += cnt
        else:
            result += 1
    stack.append(i)
print(result)