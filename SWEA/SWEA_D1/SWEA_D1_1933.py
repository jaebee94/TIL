# 1933. 간단한 N 의 약수

def yaksu(num):
    result = ''
    for i in range(1, num+1):
        if not num % i:
            result += str(i) + ' '
    return result

number = int(input())
print(yaksu(number))