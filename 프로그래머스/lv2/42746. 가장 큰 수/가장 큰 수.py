def solution(numbers):
    answer = ''
    data_list = []
    for k,i in enumerate(numbers):
        data = (str(i)*6)[:6]
        data_list.append([k,data])
    data_list = sorted(data_list, key=lambda x:x[1], reverse=True)
    for i,j in data_list:
        answer += str(numbers[i])
    answer = str(int(answer))
    return answer