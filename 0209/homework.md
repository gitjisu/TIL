```
T = 10
for tc in range(1, T+1):
    N = int(input())  # len(arr)
    arr = list(map(int, input().split()))
    total = 0

    for i in range(2, N-2):
        max_value = 0
        for j in (arr[i+1], arr[i+2], arr[i-1], arr[i-2]):
            if j > max_value:
                max_value = j
        if arr[i] > max_value:
            total += arr[i] - max_value
    print(f'#{tc} {total}')
```

