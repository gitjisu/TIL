```
import sys
sys.stdin = open('1.txt')

def bfs():
    check = 0
    temp = [0]
    v[0] = 1
    while len(temp) != 0:
        idx = temp.pop(0)
        for w in range(2):
            if board[idx][w] != -1 and v[board[idx][w]] == 0:
                temp.append(board[idx][w])
                v[board[idx][w]] =1
                if board[idx][w] == 99:
                    temp = []
                    check = 1
                    break
    return check


for t in range(1,11):
    tc, n = map(int, input().split())
    road = list(map(int, input().split()))
    board = [[-1, -1] for _ in range(100)]
    v = [0] * 100
    for q in range(n):
        if board[road[2*q]][0] == -1:
            board[road[2 * q]][0] = road[2*q+1]
        else:
            board[road[2*q]][1] = road[2*q+1]
    res = bfs()
    print(f'#{tc} {res}')
```

