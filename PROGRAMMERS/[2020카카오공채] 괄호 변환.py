def solution(p):
    global u, v, tmp, answer
    # answer = ''
    left = right = 0
    tmp=''
    for i in p:
        tmp += i
        if i == '(':
            left += 1
        else:
            right += 1
        if left == right:
            u = tmp
            for i in u:
                if i == '(':
                    confirm += 1
                else:
                    confirm -= 1
                if confirm < 0:
                    tmp = '(' + solution(v) + ')'
                    print(tmp, u)
                    for j in u[1:-2]:
                        if j == '(':
                            tmp += ')'
                        else:
                            tmp += '('
                else:
                    return u + solution(p[2*left:len(p)])
            v = p[2*left:len(p)]
            break

    confirm = 0
    print('u',u, 'v',v)
    for i in u:
        if i == '(':
            confirm += 1
        else:
            confirm -= 1
        if confirm < 0:
            tmp = '(' + solution(v) + ')'
            print(tmp, u)
            for j in u[1:-2]:
                if j == '(':
                    tmp += ')'
                else:
                    tmp += '('
            print(tmp)
            return tmp
    if v:
        print(u, v)
        answer = u + solution(v)
    else:
        return u
    return answer

print(solution("()))((()"))