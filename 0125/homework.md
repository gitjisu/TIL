```
.sort()
원본 리스트를 정렬하되 반환 값 None
원본 리스트의 순서 변경
sorted보다 빠름

sorted()
정렬된 새로운 리스트 반환 원본 영향x
모든 iterable에 동작 가능
```



```
append()
리스트 마지막에 추가, 리스트를 넣어도 그 형태로 추가됨

extend()
리스트 속에 있는 요소들이 추가 됨
```



```
b = a 얕은복사 
얕은 복사의 경우 a의 요소만 바꾸려고 해도 b까지 같이 바뀜(주소같음)

깊은 복사로 진행하면 원본에 영향x
b = a.copy()
b = a[:]
```

