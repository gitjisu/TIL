```
for _ in range(10) :
    tc = int(input())
    arr = list(map(int,input().split()))
    cnt = 1
    while True:
        temp = arr.pop(0) - cnt
        if temp <= 0:
            arr.append(0)
            break
        arr.append(temp)
        cnt += 1
        if cnt == 6:
            cnt = 1
    print(f'#{tc}',*arr)
```

