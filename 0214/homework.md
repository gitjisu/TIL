```
T = 10
N = 100
for tc in range(1, T+1):
    no = int(input())
    array = [list(map(int, input().split())) for _ in range(N)]


    max_value = 0

    for i in range(N):
        sum_value = 0
        for j in range(N):
            sum_value += array[i][j]
        if max_value < sum_value:
            max_value = sum_value


    for i in range(N):
        sum_value = 0
        for j in range(N):
            sum_value += array[j][i]
        if max_value < sum_value:
            max_value = sum_value

    sum_value = 0
    for i in range(N):
        sum_value += array[i][i]
        if max_value < sum_value:
            max_value = sum_value


    sum_value = 0
    for i in range(N):
        sum_value += array[i][N-1-i]

        if max_value < sum_value:
            max_value = sum_value

    print("#{} {}".format(no, max_value))
```



