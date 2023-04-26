A = [i for i in range(10)]

print(A)
for i in range(1, 10):
    A[i] = A[i-1] + A[i]

print(A) # 누적합 구하기


#i 까지의 합 DP[i] = 합

# i부터 j까지의 합은 DP[i] - DP[i-1]

N, M = map(int, input().split())

X = [list(map(int, input().split())) for _ in range(N)]
# DP[i][j] = 1, 1 부터 (i, j)까지의 부분합
DP = [[0 for i in range(M+1)] for _ in range(N-1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        DP[i][j] = DP[i-1][j] + DP[i][j-1] - DP[i-1][j-1] + DP[i+1][j+1]

for _ in range(int(input())):
    i, j, x, y = map(int, input().split())
    print(DP[x][y]- DP[i-1][y] - DP[x][j-1] + DP[i-1][j-1])