import base64

testcase = int(input())

for T in range(testcase):
    s = str(input())

    s1 = s.encode("UTF-8")
    d = base64.b64decode(s1)
    s2 = d.decode("UTF-8")
    print('#{} {}'.format(T+1, s2))
