# 2029. 몫과 나머지 출력하기

def division(i, j):
    m = i // j
    r = i % j
    return str(m) + ' ' + str(r)

testcase = int(input())
for T in range(testcase):
    i, j = map(int, input().split())
    print('#{} {}'.format(T+1, division(i, j)))
