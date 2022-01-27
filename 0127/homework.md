```
28.259999999999998
18.84
```

```
class Dog(Animal):
    def __init__(self,name):
        self.name = name

    def walk(self):
        print(f'{self.name}! 달린다!')

    def bark(self):
        print(f'{self.name}! 짖는다!')

class Bird(Animal):
    def __init__(self,name):
        self.name = name

    def fly(self):
        print(f'{self.name}! 푸드덕!')
```

```
ZeroDivisionError: 어떤 수를 0으로 나눴을 때
NameError: 지역 혹은 전역 이름 공간 내에서 유효하지 않는 이름을 사용했을때, 즉 어느 곳에서도 정의되지 않은 변수를 호출 하였을때
TypeError: 자료형이 올바르지 않을경우
IndexError: 존재하지 않는 index로 조회할 경우
KeyError: 존재하지 않는 Key로 접근한 경우
ModuleNotFoundError: 존재하지 않는 Module을 import 하는 경우
ImportError: Module은 찾았으나 존재하지 않는 클래스/함수를 가져오는 경우
```

