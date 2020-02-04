testcase = int(input())

for T in range(testcase):
    number0 = int(input())
    N = [2, 3, 5, 7, 11]
    alist = [-1]*5
    for m in range(len(N)):
        number = number0
        while (number % 1) > 1 or number % 1 == 0:
            alist[m] += 1
            number = number / N[m]
        alist[m] = str(alist[m])
    print('#{} {}'.format(T+1, ' '.join(alist)))