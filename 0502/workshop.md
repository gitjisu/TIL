```
<body>
  <h1>Dog API</h1>
  <img src="" alt="dog">
  <br>
  <button>Get dog</button>

  <!-- axios CDN을 삽입한다. -->
  <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
  <script>
    const API_URI = 'https://dog.ceo/api/breeds/image/random'

    function getDog() {
      // axios를 사용하여 API_URI로 GET 요청을 보낸다.
      axios.get(API_URI)

      // .then 메서드를 통해 요청이 성공적인 경우의 콜백함수를 정의한다.
        .then(function (res) {
          const image = res.data.message
          
          // 응답객체의 데이터에서 이미지에 대한 리소스를 img 요소의 src 속성으로 할당한다.           
          const imgTag = document.querySelector('img')
          imgTag.setAttribute('src', image)
        })
    }
    
    const button = document.querySelector('button')
    button.addEventListener('click', getDog)
    
  </script>
</body>
```

