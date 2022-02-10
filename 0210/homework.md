```

def max_v():
    max_value = 0
    max_index = 0
    for i in range(len(box)):
        if box[i] > max_value:
            max_value = box[i]
            max_index = i
    return max_index

def min_v():
    min_value = 101
    min_index = 0
    for i in range(len(box)):
        if box[i] < min_value:
            min_value = box[i]
            min_index = i
    return min_index



T = 10
for tc in range(1, 11):
    N = int(input())
    box = list(map(int, input().split()))


    for i in range(N):
        box[max_v()] -= 1
        box[min_v()] += 1

    result = box[max_v()] - box[min_v()]
    print(f'#{tc} {result}')






```

