```
int
float
str
list
dict
```

```
__init__ :생성자! 첫 번째 인수로 self를 지정받아야 함, 컨스트럭터라고 불리며 초기화를 위해 사용, 인스턴스화를 실시할 때 반드시 처음에 호출되는 특수한 함수
__del__: 소멸자! 인스턴스가 사라질 때 호출
__str__:해당 클래스로 만들어진 인스턴스 자체를 출력할 때 문자열로 설명해주기 위함 , 서로 다른 자료형 간 인터페이스를 제공하기 위함(문자열화하여 반환)(프린트와같음)
__repr__:객체를 인간이 이해하기 쉽도록 평문으로 표현하는것, 오피셜

```

``` 
문자열
upper/lower: 대문자,소문자변경
swapcase(): 대문자는 소문자로 소문자는 대문자로
capitalize(): 첫문자를 대문자로 
title : 각 단어의 첫 글자를 대문자로

리스트
sort: none을 반환하며 리스틀 요소대로 반환한다
reverse: none을 반환하며 요소를 역순으로 배열한다
index(x) : 리스트에 x가 등장하는 첫 위치 반환 x가 없을경우 valueError 발생 프로그램 중단
insert(i,x) : 리스트의 i번째 위치에 x를 삽입한다
remove(x) : 리스트에서 첫번째로 나오는  x를 찾아 삭제

딕셔너리
keys() : 변수 내 모든 키값 출력(리스트형태로)
values : 변수 내 모든 벨류 값 출력(리스트형태로)
items : 변수 내 모든 키 + 값 출력(리스트형태로)
has_key : 변수 내 해당 키 값이 존재하냐? (T/F)
[key] : 해당 키 값에 해당하는 value값 조회 (에러o)
.get(key) : 해당 키 값에 해당하는 value값 조최 (에러x)
[key] = value : 변수 내 키+value 추가
del딕셔너리변수[key] : 변수 내 키+value 삭제
```

```
from fibo.py import fibo_recursion as recursion
```

