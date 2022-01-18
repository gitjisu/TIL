#### 1. 간단한 N의 약수 

```
[제약 사항]
N은 1이상 1,000이하의 정수이다. (1 ≤ N ≤ 1,000)
[입력]
입력으로 정수 N이 주어진다.
[출력]
정수 N의 모든 약수를 오름차순으로 출력한다.
[입력 예시]
10
[출력 예시]
1 2 5 10


N = int(input())

for i in range(1,N+1):
	if N % i == 0 :
		print(i, end='')


```





#### 2.중간값 찾기 

```
a = [
	85, 72, 38, 80, 69, 68, 96, 22, 49, 67,
	51, 61, 63, 87, 66, 24, 80, 83, 71, 60, 64, 
    52, 90, 60, 49, 31, 23, 99, 94, 11, 25, 24
]


a.sort()
median = 0
idx = 0

if len(a)%2 == 0:
	idx = len(a)//2
	median = (a[idx-1]+a[idx])/2
	

else:
	idx = len(a)//2+1
	median = a[idx]
	
print("리스트의 중간값은 {}입니다.".format(median))
```





#### 3. 계단 만들기

```
n = int(input())
for i in range(n): 
    line_str = "" 
    for j in range(i+1):
        line_str += str(j+1) 
    print(line_str)
	
```

