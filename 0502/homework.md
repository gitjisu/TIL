### 1. 아래의 설명을 읽고 T/F 여부를 작성하시오.

\-	JavaScript는 single threaded 언어로 한 번에 한 가지 일 밖에 처리하지 못한다.	(T)

\-	setTimeout은 브라우저의 Web API를 사용하는 함수로, Web API에서 동작이 완료되면 Call Stack에 바로 할당된다.	(F)



### 2. JavaScript에서 동기와 비동기 함수의 차이점을 서술하시오.

동기 : 위의 작업을 완료하지 않았다면 밑에 작업을 수행하지 않고 순차적으로 수행한다.

비동기: 위의 작업이 끝나지 않았어도 밑에 작업을 수행한다.



### 3. 다음은 axios를 사용하여 API 서버로 요청을 보내고, 정상적으로 응답이 왔을 때 응답 데이터를 출력하는 코드이다. (a), (b), (c)에 들어갈 코드를 작성하시오.

```html
axios.(a)('https://api.example.com/data')
	.(b)(funcion (response) {
         console.log((c))
    })

(a) : get
(b) : then
(c) : response.data
```

