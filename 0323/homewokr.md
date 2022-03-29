```
num = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
         '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}
 
def find_1(arr):
    global Data
    for y in range(N):
        for x in range(M-1, -1, -1):
            if arr[y][x] == '1':
                Data = arr[y][x-55:x+1]
                return Data
 
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    Data = ''
    find_1(arr)
 
    result = []
    start = 0
    end = 6
    for _ in range(8):
        result.append(num[Data[start:end+1]])
        start += 7
        end += 7
 
    value = (result[0] + result[2] + result[4] + result[6])*3 + (result[1]+result[3]+result[5]) + result[7]
 
    if not value % 10:
        print(f'#{tc} {sum(result)}')
    else:
        print(f'#{tc} 0')
```

