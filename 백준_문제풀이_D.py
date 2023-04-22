from copy import deepcopy

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
Q = [tuple(map(int, input().split())) for _ in range(K)]
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
ans = 10000

def value(arr):
    return min([sum(i) for i in arr])

def convert(arr, qry):
    (r, c, s) = qry
    r, c= r-1, c-1
    new_arr = deepcopy(arr)
    for i in range(1, s+1):
        rr, cc = r-1, c+i
        for w in range(4):
            for d in range(i*2):
                rrr, ccc = rr + dx[w], cc + dy[w]
                new_arr[rrr][ccc] = arr[rr][cc]
                rr, cc = rrr, ccc


def dfs(arr, qry):
    if sum(qry) == K: # 쿼리를 다 사용
        ans = min(ans, value(arr))
        return
    for i in range(K):
        if qry[i]: # 쿼리 처리 시
            continue
        new_arr = convert(arr, Q[i]) # 처리한 쿼리를 새로운 배열로 반환
        qry[i] = 1
        dfs(new_arr, qry)
        qry[i] = 0

dfs(A, [0 for i in range(K)])

print(ans)

#bitmask 기법
#1,2 5, --> 10진수 (처리 순서)
#10011 --> 2진수

#1, 2, 3, 4, 5, 6, 7
#1, 2, 4, 8, 16, 32, 64


# 1, 2, 3, 4, 5, 6, 7 작업 우선 1, 3, 5 사용
# set{1,2,3,4,5,6,7} 
# 1, 3, 5 -> 처리 후 -> 2, 4, 6, 7 처리

# 시간 복잡도 : 50 * 50 * 6 * 720