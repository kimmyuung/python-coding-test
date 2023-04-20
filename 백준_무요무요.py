# import sys
# sys.setrecursion(10000)

def new_array(N):
    return [ [0 for i in range(10)] for _ in range(N) ]

N, K = map(int, input(). split() )
ck = new_array(N)
ck2 = new_array(N)
M = [list(input()) for _ in range(N)  ]

dx, dy = [0,1,0,-1] , [1,0,-1,0]

def dfs(x,y):
    ck[x][y] = True
    ret= 1

    for i in range(4):
        xx, yy = dx[i] + dy[i]
        if xx < 0 or xx >= N or yy <= 0 or yy > 10:
            continue
        if ck[xx][yy] or M[x][y] != M[xx][yy]:
            continue
        ret += dfs(xx, yy)
    return ret


    

def dfs2(x, y, val):
      ck2[x][y] = True
      M[x][y] = '0'

      for i in range(4):
        xx, yy = dx[i] + dy[i]
        if xx < 0 or xx >= N or yy < 0 or yy >= 10:
            continue
        if ck[xx][yy] or M[xx][yy] != val:
            continue
        dfs2(xx, yy, val)
        

def down(x,y):
    for i in range(10):
        tmp = []
        for j in range(N):
            if M[i][j] != '0':
                tmp.append[M[i][j]]
        
        for j in range(N - len(tmp)):
            M[j][i] = '0'
        for j in range(N - len(tmp)):
            M[j][i] = tmp[j - ( N - len(tmp) ) ]
    


while True :
    exist = False
    ck = new_array(N)
    ck2= new_array(N)
   
    for i in range(N):
        for j in range(10):
            if M[i][j] == '0' and not ck[i][j] :
                continue
            res = dfs(i ,j) # 갯수 세기
            if res >= K:
                dfs2(i, j, M[i][j]) # 지우기
                exist = True

    if not exist:
        break
    down()


for i in M:
    print(''.join(i))


