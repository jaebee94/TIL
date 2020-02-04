# 2056. 연월일 달력

testcase = int(input())
month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
big = [1, 3, 5, 8, 10, 12]
small = [4, 6, 9, 11]

for T in range(testcase):
    date = str(input())
    if int(date[4:6]) in big and int(date[6:8]) > 31:
        result = -1
    elif int(date[4:6]) in small and int(date[6:8]) > 30:
        result = -1
    elif int(date[4:6]) == 2 and int(date[6:8]) > 28:
        result = -1
    elif int(date[4:6]) not in month:
        result = -1
    else:
        date = [date[0:4], date[4:6], date[6:8]]
        result = '/'.join(date)
    print('#{} {}'.format(T+1, result))