import math
def solution(progresses, speeds):
    answer = []
    progresses = [math.ceil((100 - j)/speeds[i]) for i, j in enumerate(progresses)]
    tmp = progresses.pop(0)
    cnt = 1
    print(tmp)
    for i in progresses:
        print(i)
        if i <= tmp:
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
            tmp = i
    answer.append(cnt)
    return answer