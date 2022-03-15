```

import sys
sys.stdin = open('1.txt')

move_list = [(1, 0), (-1, 0), (0, 1), (0, -1)]
 
def dfs(y, x):
    global result
    if map_list[y][x] == 3: # 도착지점이면 
        result = 1 # 결과 1로 바꾸고 리턴
        return
    for i, j in move_list: # 4방향 이동
        dy = y + i
        dx = x + j
        if map_list[dy][dx] != 1 : # 1이아닐때만
            map_list[y][x] = 1 # 1로 바꿔주고 재귀호출
            dfs(dy, dx)			
        
 
T = 10
for _ in range(T):
    t = int(input())
    N = 16
    map_list = [list(map(int, list(input()))) for _ in range(N)]
    result = 0 # 아니면 0
    dfs(1,1) # 1,1에서 시작
    print(f'#{t} {result}')

```

