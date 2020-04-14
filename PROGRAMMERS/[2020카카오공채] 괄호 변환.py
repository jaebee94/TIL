def solution(p):
    tmp = ''
    left = right = 0
    if not p:
        return ''
    else:
        for i in p:
            tmp += i
            if i == '(':
                left += 1
            else:
                right += 1
            if left == right:
                u = tmp
                v = p[2*left:len(p)]
                break
        confirm = 0
        for i in u:
            if i == '(':
                confirm += 1
            else:
                confirm -= 1
            if confirm < 0:
                tmp = '(' + solution(v) + ')'
                for j in u[1:-1]:
                    if j == '(':
                        tmp += ')'
                    else:
                        tmp += '('
                return tmp
        return u + solution(v)

print(solution("()))((()"))