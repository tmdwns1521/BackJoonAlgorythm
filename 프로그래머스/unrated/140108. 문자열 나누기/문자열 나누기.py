def solution(s):
    answer = 0
    s = list(s)
    cnt = 0
    stack = []
    while s:
        da = s.pop(0)
        if stack and stack[0] == da:
            cnt += 1
        elif not stack:
            stack.append(da)
            cnt += 1
        else:
            cnt -= 1
            if cnt == 0:
                stack.pop()
                answer += 1
    if stack:
        answer += 1
    return answer