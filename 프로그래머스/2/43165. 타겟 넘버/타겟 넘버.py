def dfs(index, sum, numbers, target):
    if index == len(numbers):
        if sum == target:
            return 1
        else:
            return 0
    count = dfs(index + 1, sum + numbers[index], numbers, target)
    count += dfs(index + 1, sum - numbers[index], numbers, target)
    
    return count

def solution(numbers, target):
    return dfs(0, 0, numbers, target)