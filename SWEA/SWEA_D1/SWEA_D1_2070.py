# 2070. 큰 놈, 작은 놈, 같은 놈
def compare(numbers):
    if numbers[0] > numbers[1]:
        result = '>'
    elif numbers[0] < numbers[1]:
        result = '<'
    else:
        result = '='
    return result

testcase = int(input())

for T in range(testcase):
    numbers = list(map(int, input().split()))
    print('#{} {}'.format(T+1, compare(numbers)))