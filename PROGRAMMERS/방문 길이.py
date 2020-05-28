def solution(dirs):
    answer = 0
    i, j = 0, 0
    di = [1, 0, -1, 0]
    dj = [0, -1, 0, 1]
    dir_list = ['R', 'D', 'L', 'U']
    path = [(0, 0)]
    for dir in dirs:
        flag = False
        for k in range(4):
            if dir == dir_list[k] and -5 <= i+di[k] <= 5 and -5 <= j+dj[k] <= 5:
                i += di[k]
                j += dj[k]
                path.append((i, j))
                # len(path) 가 3이하일 때 판단 불가
                for x in range(len(path)-2):
                    # print(path[x:x+2], path[-1:-3:-1])
                    if path[x:x+2] == path[-2:] or path[x:x+2] == path[-1:-3:-1]:
                        flag = True
                        break
                if flag:
                    break
                else:
                    answer += 1
                    break
    return answer