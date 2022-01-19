#### 1. List의 합 구하기

정수로만 이루어진 list를 전달 받아 해당 list의 모든 요소들의 합을 반환하는 list_sum
함수를 built-in 함수인 sum() 함수를 사용하지 않고 작성하시오

```
list = [1, 2, 3, 4, 5]

def sum(list):
    sum = 0
    for i in list:
        sum += i
    return sum

print(sum(list))
```





#### 2. Dictionary로 이루어진 List의 합 구하기

Dictionary로 이루어진 list를 전달 받아 모든 dictionary의 'age' key에 해당하는 value 들의 합을 반환하는 dict_list_sum 함수를 built-in 함수인 sum() 함수를 사용하지 않고 작성하시오.

```
dict_list = {'name' : 'kim', 'age' : 12}, {'name' : 'lee', 'age' : 4}

sum = 0
for dic in dict_list:
    sum += dic['age']

print(sum)
```





#### 3. 2차원 List의 전체 값 구하기

정수로만 이루어진 2차원 list를 전달 받아 해당 list의 모든 요소들의 합을 반환하는 all_list_sum 함수를 built-in 함수인 sum() 함수를 사용하지 않고 작성하시오.

```

list = [[1],[2,3],[4,5,6],[7,8,9,10]]

def sum(list):
    sum = 0
    for i in list[0]:  
        sum += i
    for i in list[1]:
        sum += i
    for i in list[2]:
        sum += i
    for i in list[3]:
        sum += i
    return sum

print(sum(list))

```

