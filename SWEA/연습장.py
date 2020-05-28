def working(i, works):
    for x in range(i):
        works[x] -= 1
        n -= 1
        print(n, works)
        

def solution(n, works):
    stress = 0
    works.sort(reverse=True)
    while True:
        for i in range(1, len(works)):
            if works[0] != works[i]:
                working(i, works)
                if n == 0:
                    for work in works:
                        stress += work ** 2
                    return stress
                break

    #     for x in range(len(works)):
    #         works[x] -= 1
    #         n -= 1
    #         print(n, works)
    #         if n == 0:
    #             for work in works:
    #                 stress += work ** 2
    #             return stress
    # return 0


print(solution(4, [4, 3, 3]))
# 12
print(solution(1, [2, 1, 2]))
# 6
print(solution(3, [1,1]))
# 0