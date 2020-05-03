def solution(begin, target, words):
    answer = 0
    visited = [False for _ in range(len(words))]
    q = []
    q.append(begin)
    while q:
        answer += 1
        loop = len(q)
        for _ in range(loop):
            begin = q.pop(0)
            for i in range(len(words)):
                cnt = 0
                # 변환할 수 있는지 체크
                for j in range(len(begin)):
                    if begin[j] != words[i][j]:
                        cnt += 1
                    if cnt > 1:
                        break
                if visited[i] == False and cnt == 1:
                    visited[i] = True
                    q.append(words[i])
                    if words[i] == target:
                        return answer
    return 0