
# Input 
C, M = list(), list()

# Milk input
for i in range(3):
    a, b = map(int, input(). split())
    C.append(a)
    M.append(b)

# Start
for i in range(100):
    idx = i % 3
    nxt = (idx+1) % 3
    M[nxt] , M[idx]= max( M[idx] - ( C[nxt] - M[nxt] ), 0), min(C[nxt], M[nxt] + M[idx])
    
for i in M:
    print(i)


