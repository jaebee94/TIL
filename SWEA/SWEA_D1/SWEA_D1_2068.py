# 2068. 최대수 구하기

def biggest(numbers):
    maximum = 0
    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum

testcase = int(input())
for T in range(testcase):
    numbers = list(map(int, input().split()))
    print('#{} {}'.format(T+1, biggest(numbers)))