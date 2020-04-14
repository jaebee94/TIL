def solution(s):
    mincnt = len(s)
    # 문자열 자르기
    n = 1
    while n <= len(s)//2:
        comp = []
        for i in range(0, len(s), n):
            nstr = str()
            for j in range(i, i+n):
                if j == len(s):
                    break
                else:
                    nstr += s[j]
            comp.append(nstr)
        # 문자열 비교
        cnt, cnt1, cnt2= 0, 1, 0
        for i in range(len(comp)-1):
            if comp[i] == comp[i+1]:
                cnt += 1
                cnt1 += 1
            # breakpoint
            else:
                if cnt1 < 10:
                    cnt2 += 1
                elif 10 <= cnt1 < 100:
                    cnt2 += 2
                elif 100 <= cnt1 < 1000:
                    cnt2 += 3
                elif 1000 <= cnt1:
                    cnt2 += 4
                cnt1 = 0
        # last breakpoint
        if cnt1 < 10:
            cnt2 += 1
        elif 10 <= cnt1 < 100:
            cnt2 += 2
        elif 100 <= cnt1 < 1000:
            cnt2 += 3
        elif 1000 <= cnt1:
            cnt2 += 4
        # 최솟값 계산
        if len(comp[-1]) == len(comp[-2]):
            a = n*(len(comp)-cnt) + cnt2
        else:
            a = n*(len(comp)-cnt-1) + cnt2 + len(comp[-1])
        if a < mincnt:
            mincnt = a
        n += 1
    answer = mincnt
    return answer
    
print(solution('abbbaccc'))
print(solution('aabbaccc'))
print(solution('ababcdcdababcdcd'))    
print(solution('abcabcdede'))
print(solution('abcabcabcabcdededededede'))
print(solution('xababcdcdababcdcd'))
print(solution('aaaaaaaaaaaaaaa'))