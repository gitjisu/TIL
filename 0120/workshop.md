#### 1. 숫자의 의미

정수로 이루어진 list를 전달 받아, 각 정수에 대응되는 아스키 문자를 이어붙인 문자열을 반환하는 get_secret_word 함수를 작성하시오. 단, list는 65이상 90이하 그리고 97이상 122이하의 정수로만 구성되어 있다.

```\
def get_secret_word(a):
    total = str( )
    for i in a:
        total += chr(i)
    return total
    
print(get_secret_word([83, 115, 65, 102, 89]))
```



#### 2. 내 이름은 뭘까?

문자열을 전달 받아 해당 문자열의 각 문자에 대응되는 아스키 숫자들의 합을 반환하는 get_secret_number 함수를 작성하시오. 단, 문자열은 A~Z, a~z로만 구성되어 있다



```
def get_secret_number(a):
    total = int ()
    for i in a:
        total += ord(i)
    return total

print(get_secret_number('tom'))
```





#### 3. 강한 이름

문자열 2개를 전달 받아 두 문자열의 각 문자에 대응되는 아스키 숫자들의 합을 비교하 여 더 큰 합을 가진 문자열을 반환하는 get_strong_word 함수를 작성하시오.

```
def get_strong_word(a, b):
    total_1 = total_2 = int ()
    for i in a:
        total_1 += ord(i)   
    for j in b:
        total_2 += ord(j)
    if total_1 > total_2 :
        return a
    else: 
        return b

print(get_strong_word('z','a'))
print(get_strong_word('tom','john'))
```

