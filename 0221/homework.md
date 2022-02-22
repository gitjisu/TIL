```
T = int(input())
for tc in range(1, T+1):
    N = int(input())
 
    pas = [[1], [1, 1]]
    for i in range(2, N):
        new = [1]
        for j in range(i-1):
            new += [pas[i-1][j] + pas[i-1][j+1]]
        new += [1]
        pas += [new]
    print(f'#{tc}')
    for i in range(N):
        print(*pas[i])
```

