# 1986. 지그재그 숫자

testcase = int(input())

for T in range(testcase):
    num = int(input())
    summ = 0
    for i in range(1, num+1):
        if i % 2:
            summ += i
        else:
            summ -= i
    print('#{} {}'.format(T+1, summ))