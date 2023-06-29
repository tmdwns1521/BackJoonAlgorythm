from collections import deque

num = int(input())
command = list(map(int, (input().split(' '))))
count_list = [0] * 1000001
for i in command:
    count_list[i] = count_list[i] + 1
result = [-1] * num
stack = [0]
for i in range(1, num):
    while stack and count_list[command[stack[-1]]] < count_list[command[i]]:
        result[stack.pop()] = command[i]
    stack.append(i)
print(*result)