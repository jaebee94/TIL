# 10989_수정렬하기3
##########메모리초과#############
N = int(input())
A = [int(input()) for _ in range(N)]
B = [0]*len(A)
C = [0]*(max(A)+1)
for i in A:
    C[i] += 1
for i in range(1, len(C)):
    C[i] += C[i-1]
for i in range(len(A)-1, -1, -1):
    B[C[A[i]]-1] = A[i]
    C[A[i]] -= 1
for num in B:
    print(num)