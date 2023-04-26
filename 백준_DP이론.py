# DP 이론(다이내믹 프로그래밍)

# 피보나치, Knaspack

# 푸는 순서

# 1. 상태를 정의

# 2. 점화식을 찾음

# 3. 시간복잡도를 계산

# 4. 코딩한다

import copy

N, A = int(input()), list(map(int, input().split()))

# DP[i] = i 까지 왔을 때, 합의 최대

DP = copy.deepcopy(A)
rev = [0 for _ in range(N)]

idx = 0

for i in range(1, N):
    for j in range(i):
        if A[i] > A[j] and DP[i] < A[i] + DP[j]:
            DP[i] = A[i] + DP[j]
            rev[i] = j
           # DP[i] = max(A[i] + DP[j], DP[i])
        if DP[idx] < DP[i]:
            idx = i

print(max(DP))



print(DP[idx])
while rev[idx] != idx:
        print(A[idx], sep=" ")
        idx = rev[idx]
    
print(A[idx])