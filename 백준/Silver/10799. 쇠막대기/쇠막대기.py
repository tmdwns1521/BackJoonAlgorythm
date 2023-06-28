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
        pop_data = stack.pop()
        if pop_data == "(":
            result += cnt
        else:
            result += 1
        stack.append(pop_data)
    stack.append(i)
print(result)