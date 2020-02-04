# 2072. 홀수만 더하기

testcase = int(input())

for T in range(testcase):
    numbers = list(map(int, input().split()))
    summ = 0
    for num in numbers:
        if num % 2:
            summ += num
    
    print('#{} {}'.format(T+1, summ))