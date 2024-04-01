import math

def solution(n, a, b, answer = 0):
    answer += 1
    
    if (((a > b) and a % 2 == 0) or (a < b) and b % 2 == 0) and abs(a - b) == 1:
        return answer
    
    a = math.ceil(a / 2)
    b = math.ceil(b / 2)
    
    return solution(n, a, b, answer)