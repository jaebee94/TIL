# 2043. 서랍의 비밀번호

pw = list(map(int, input().split()))

# 비밀번호 P는 000~999 중 하나
# K 부터 1씩 증가하며 비밀번호 확인

cnt = pw[0] - pw[1] + 1
print(cnt)