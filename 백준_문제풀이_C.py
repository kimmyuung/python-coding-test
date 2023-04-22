from copy import deepcopy # 주소는 복사하지 않고 내용만 복사

# 파이썬에서는 =를 사용하여 대입시 변수의 메모리 주소가 똑같아짐

def rotate90(B, N):
    NB = deepcopy(B)
    for i in range(N):
        NB[j][N-i-1] = B[i][j]
    return NB

def convert(lst, N):
   new_list = [i for i in lst if i ]
   for i in range(1, len(new_list)):
       if new_list[i-1] == new_list[i]:         
                new_list[i-1] *= 2
                new_list[i] = 0
   new_list = [i for i in lst if i ]
   return new_list + [0] * (N-len(new_list))

N = int(input())

Borrd = [list(map(int, input().split()) for i in range(N))]
 
def dfs(N, Board, count):
    ret = max([max[i] for i in Board])
    if count == 0:
        return ret
    
    for _ in range(4):
        X = [convert(i, N) for i in Board]
        if X != Board:
            ret = ax(ret, dfs(N, X, count-1))
        Board = rotate90(Board, N)
    return ret   

print(dfs(N, Board, 5))

#        BoardCopy = deepcopy(Board)
