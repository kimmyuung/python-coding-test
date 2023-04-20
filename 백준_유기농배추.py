import sys
sys.setrecursionlimit(10000) # 깊이 제한 없을 시 런타임 에러 발생 

T = int (input())
B, ck = [], []

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

def dfs(x, y):
    global B, ck

    if ck[x][y] == 1:
        return # 디버깅 용

    ck[x][y] = 1
    for i in range(4):
        xx, yy = x + dx[i], y + dy[i]
        if B[xx][yy] == 0 or ck[xx][yy] :
            continue
        
        dfs(xx, yy)


def process():
    global B, ck

    M, N, K = map(int, input().split())
    B = [[0 for i in range(50+2)] for _ in range(50+2)] # 최대 배열 선언 
    ck = [[0 for i in range(50+2)] for _ in range(50+2)] # 최대 배열 선언
    for _ in range(K):
        X, Y = map(int, input().split())
        B[X+1][Y+1] = 1
    ans = 0
    for i in range(1, N+1):
        for j in range(1, M+1):
            if B[i][j] == 0 or ck[i][j] :
                continue
            dfs(i, j)
            ans += 1
    print(ans)


for _ in range(T):
    process()