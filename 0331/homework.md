```
def percent(people, result):
    global answer
 
    if people == N:
        if result > answer:
            answer = result
            return
 
    if result <= answer:
        return
 
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            percent(people+1, result * arr[people][i] * 0.01)
            visited[i] = 0
 
 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    answer = 0
 
    percent(0, 1)
    print(f'#{tc} {answer*100:.6f}')

```

