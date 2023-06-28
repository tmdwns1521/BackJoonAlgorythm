num = int(input())
result = [-1] * num
lists = list(map(int, input().split(' ')))
stack = [0]
for i in range(1, num):
    while stack and lists[stack[-1]] < lists[i]:
        result[stack.pop()] = lists[i]
    stack.append(i)
print(*result)