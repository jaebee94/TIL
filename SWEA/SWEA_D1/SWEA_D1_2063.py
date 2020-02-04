# 2063. 중간값 찾기

# 중간값은 통계 집단의 수치를 크기 순으로 배열 했을 때 전체의 중앙에 위치하는 수치를 뜻한다.
# 입력으로 N 개의 점수가 주어졌을 때, 중간값을 출력하라

def median(N, score):
    idx = len(score) // 2

    for i in range(len(score)-1, 0, -1):
        for j in range(0, i):
            if score[j] > score[j+1]:
                score[j], score[j+1] = score[j+1], score[j]
        if i == idx:
            return score[j+1]

N = int(input())
score = list(map(int, input().split()))
print(median(N, score))

    
