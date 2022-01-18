#### 1. Mutable & Immutable 주어진 컨테이너들을 각각 변경 가능한 것(mutable)과 변경 불가능한 것(immutable)으로 분류하시오

mutable : 리스트, 세트, 딕셔너리

immutable : 튜플, 레인지





#### 2. 홀수만 담기 range와 slicing을 활용하여 1부터 50까지의 숫자 중, 홀수로만 이루어진 리스트를 만드시오

```
print(list(range(1,51,2)))
```



#### 3. Dictionary 만들기 반 학생들의 정보를 이용하여 key는 이름, value는 나이인 dictionary를 만드시오.

```
dict_class ={'김남준' : '29', '김석진' : '31', '제이홉' : '29', '민윤기' : '30', '박지민' : '27' ,'김태형' : '27', '전정국' : '26'}
```



#### 4. 반복문으로 네모 출력

```
# 두 개의 정수 n과 m이 주어졌을 때, 가로의 길이가 n, 세로의 길이가 m인 직사각형 형태를
별(*) 문자를 이용하여 출력하시오. 단, 반복문을 사용하여 작성하시오


n = int(input())
m = int(input())

for i in range(m):
	for j in range(n):
		print('*', end='')
	print()
```



#### 5. 조건 표현식

```
if temp >=37.5 '입실불가' else '입실가능'
```



#### 6. 평균 구하기

```
scores = [80, 89, 99, 83]

print(sum(scores) / len(scores))
```

