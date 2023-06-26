import sys
from collections import deque

command = sys.stdin.readline().strip()
stack = deque()
string = ''
check = True
deq = deque(command)
while deq:
    left = deq.popleft()
    if left == ' ' and check:
        if stack:
            string += "".join(stack) + " "
            stack.clear()
    else:
        if left == '<':
            if stack:
                string += "".join(stack)
                stack.clear()
            check = False
        if not check:
            string += left
        else:
            stack.appendleft(left)
        if left == '>':
            check = True
            if stack:
                string += "".join(stack)
                stack.clear()
if stack:
    string += "".join(stack)
    stack.clear()
string += " "
print(string)