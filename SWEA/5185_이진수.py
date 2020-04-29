Conversion = {'0':0,'1':1, '2':2, '3':3, '4':4,'5':5,'6':6,'7':7,'8':8, '9':9,
        'A':10,'B':11,'C':12, 'D':13,'E':14,'F':15}

def Binary(num):
    global result
    q, r = 0, 0
    for i in range(4):
        q = num // 2
        r = num % 2
        result = str(r) + result
        num = q
    return

for tc in range(1, int(input())+1):
    N, decimal_num = map(str, input().split())

    final_result = ''
    for i in decimal_num:
        result = ''
        Binary(Conversion[i])
        final_result += result
    print('#%d %s'%(tc, final_result))