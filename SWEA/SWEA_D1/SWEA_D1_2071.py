# 2071. 평균값 구하기

testcase = int(input())

def banolim(a):
    if a % 1 >= 0.5:
        return int(a - a%1 + 1)
    else:
        return int(a - a%1)

for T in range(testcase):
    summ = 0
    numbers = list(map(int, input().split()))
    for num in numbers:
        summ += num
    result = banolim(summ/len(numbers))

    print('#{} {}'.format(T+1, result))