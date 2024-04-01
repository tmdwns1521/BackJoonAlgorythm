def solution(k, tangerine):
    tangerineObject = {}
    kinds = 0
    for i in tangerine:
        if tangerineObject.get(i) is None:
            tangerineObject[i] = 0
        tangerineObject[i] += 1
    tangerineObject = sorted(tangerineObject.items(), key=lambda x: x[1], reverse=True)
    for item in tangerineObject:
        k = k - item[1]
        kinds += 1
        if k <= 0:
            break
    return kinds