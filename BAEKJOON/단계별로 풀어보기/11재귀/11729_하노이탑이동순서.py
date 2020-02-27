cnt = 0
def hanoi(block, a, b, c):
    global cnt
    if block == 1:
        process.append([a, c])
        cnt += 1
    else:
        hanoi(block - 1, a, c, b)
        process.append([a, c])
        cnt += 1
        hanoi(block - 1, b, a, c)


process = []
hanoi(int(input()), 1, 2, 3)
print(cnt)
for i in range(len(process)):
    print(' '.join(map(str, process[i])))
