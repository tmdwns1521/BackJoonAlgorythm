def solution(s, n):
    answer = ''
    for _ in s:
        if _ != ' ':
            answerN = ord(_) + n
            if (_.islower() and 97 <= answerN <= 122) or (_.isupper() and 65 <= answerN <= 90):
                pass
            else:
                answerN -= 26
            answer += (chr(answerN))
        else:
            answer += _
    return answer