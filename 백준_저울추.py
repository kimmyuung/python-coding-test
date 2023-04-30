N , A = int(input()), list(map(int, input().split())).sorted()

ans = 0

for i in range(A):
    if i <= ans + 1:
        ans += i
    else:
        break

print(ans + 1) 