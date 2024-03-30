def solution(n, ans = 0):
    if n == 1:
        return 1
    elif n % 2 == 0:
        res = int(n / 2)
    else:
        ans += 1
        res = int(n - 1 / 2)
    if res == 1:
        return ans + 1
    return solution(res, ans)