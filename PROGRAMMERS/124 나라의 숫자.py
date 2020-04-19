def solution(n):
    answer = ''
    trans = ['4', '1', '2']
    q = True
    while q:
        q = n // 3
        r = n % 3
        if not r:
            answer = '4' + answer
            q -= 1
        else:
            answer = trans[r] + answer
        n = q
    return answer