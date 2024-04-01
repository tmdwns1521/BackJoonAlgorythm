import math

def solution(n, a, b, answer = 0):
    answer += 1
    
    if max(a, b) % 2 == 0 and abs(a - b) == 1:
        return answer
    
    a = math.ceil(a / 2)
    b = math.ceil(b / 2)
    
    return solution(n, a, b, answer)