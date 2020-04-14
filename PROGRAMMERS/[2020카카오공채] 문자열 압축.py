def solution(s):
    answer = len(s) # 최소값에 대한 초기값 세팅
    for j in range(1, len(s)//2+1): # 몇 글자씩 자를지, 1~(전체길이//2)
        cnt = 1 # 중복 문자열 카운팅 초기값
        cur_len = 0 # 현재 압축된 문자 길이
        for i in range(0, len(s)-j, j): # 0부터 j 칸씩 건너뛰면서 비교
            # i부터 j개 글자 인덱싱
            if s[i:i+j] == s[i+j:i+2*j]:    # 다음 문자열 덩어리와 같은지 판단
                cnt += 1
                if i+j == len(s)-j: # 다음 문자열 덩어리가 전체 문자열의 마지막
                    cur_len += len(str(cnt)) + j    # cnt 자리수 + j
            else:   # 압축이 끝날 때
                if cnt == 1:    # 1은 생략
                    cur_len += j
                else:
                    cur_len += len(str(cnt)) + j
                cnt = 1
                if i+2*j >= len(s): # 마지막 덩어리일때
                    cur_len += len(s[i+j:i+2*j])    # 남은 문자열 더하기
        # 최소값 비교
        if answer > cur_len:
            answer = cur_len
    return answer

print(solution('aabbaccccccaa'))
print(solution('ababcdcdababcdcd'))    
print(solution('abcabcdede'))
print(solution('abcabcabcabcdededededede'))
print(solution('xababcdcdababcdcd'))
print(solution('aaaaaa'))