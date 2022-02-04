1. img tag

아래 그림과 같은 폴더 구조가 있다. resume.html에서 코드를 작성 중일 때, image  폴더 안의 my_photo.png를 보여주는 ![img]() tag를 작성하시오.  단, 이미지가 제대로 출력되지 않을 때는 ssafy 문자열이 출력 되도록 작성하시오

```
<img src="C:\Users\Window 10\Desktop\TIL\ssafy\image\my_photo.jpg"alt="ssafy"
```



2. 파일경로

위와 같이 경로를 __(a)__로 작성 할 시, github에 업로드 하거나 전체 폴더의 위치가 변경 되었을 때 이미지를 불러 올 수 없게 된다. 이를 해결 하려면 이미지 경로를 __(b)__ 로 바꾸어 작성하면 된다.  __(a)__와 __(b)__에 들어갈 말과 __(b)__ 로 변경한 코드를 작성하시오.

(a) : 절대경로

(b) : 상대경로

<img src="..\image\my_photo.jpg"alt="ssafy">



3. Hyper Link

```
<a href="ssafy.com">
<img src="../image/my_photo"alt="ssafy">
</a>
```





4. 선택자

```
:nth-child(N)= 부모안에 모든 요소 중 N번째 요소
A:nth-of-type(N)= 부모안에 A라는 요소 중 N번째 요소
```

