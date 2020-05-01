def Binary(num):
    global result, cnt
    while True:
        next = num * 2
        result += str(int(next))
        num = next - int(next)
        cnt += 1
        if num == 0.0:
            return
        if cnt > 13:
            return

for tc in range(1, int(input())+1):
    num = float(input())
    result = ''
    cnt = 0
    Binary(num)
    if cnt > 13:
        print('#{} overflow'.format(tc))
    else:
        print('#{} {}'.format(tc, result))