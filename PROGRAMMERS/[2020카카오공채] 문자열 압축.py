def solution(s):
    answer = len(s)
    for j in range(1, len(s)//2+1):
        cnt = 1
        cur_len = 0
        for i in range(0, len(s)-j, j):
            if s[i:i+j] == s[i+j:i+2*j]:
                cnt += 1
                if i+j == len(s)-j:
                    cur_len += len(str(cnt)) + j
            else:
                if cnt == 1:
                    cur_len += j
                else:
                    cur_len += len(str(cnt)) + j
                cnt = 1
                if i+2*j >= len(s):
                    cur_len += len(s[i+j:i+2*j])
        
        if answer > cur_len:
            answer = cur_len
    return answer