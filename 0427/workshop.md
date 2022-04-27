```
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    .text-decoration-none {
      text-decoration: none;
    }
  </style>
</head>

<body>
  <a id="anchor" href="">GOOGLE</a>

  <script>

    /*
      JavaScript 코드만을 활용하여 a#anchor 요소를 아래와 같이 수정합니다.
        1) a 태그에 text-decoration-none 클래스를 추가합니다.
        2) a 태그의 href 속성은 https://google.com/ 입니다.
        3) a 태그의 target 속성은 _blank 입니다. (새 탭에서 열기)
    */
    const anchor = document.querySelector('#anchor')
    anchor.setAttribute('class', 'text-decoration-none')

    anchor.href = 'https://google.com/'
    anchor.target = '_blank'
  </script>
</body>

</html>
```

```
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>

<body>

  <div id="app"></div>

  <script>
    // div#app 요소 선택
    const divApp = document.querySelector('#app')
    
    // h1 태그를 createElement 로 생성
    const h1 = document.createElement('h1')

    // 생성한 h1태그의 내용을 '오늘의 Todo' 로 설정
    h1.innerText = '오늘의 Todo'

    // ul, li 태그들을 생성 및 내용 추가
    const ul = document.createElement('ul')
    const li1 = document.createElement('li')
    li1.innerText = '양치'
    const li2 = document.createElement('li')
    li2.innerText = '공부'
    const li3 = document.createElement('li')
    li3.innerText = '휴식'
    ul.append(li1, li2, li3)
    

    // 각 태그들을 적절하기 div#app 요소에 자식요소로 추가. (#app > ul > li)
    divApp.append(h1, ul)
    



  </script>
</body>

</html>
```

```
<!DOCTYPE html>
<html lang="en">

<head>
  <title>Document</title>
  <!-- CSS only -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet"
    integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
</head>

<body>

  <div class="container">

    <section id="cardsSection" class="row">

      <!-- 카드 예시 -->
      <article class="col-4">
        <div class="card m-1">
          <div class="card-body">
            <h5 class="card-title">Example</h5>
            <p class="card-text">This is a card example.</p>
          </div>
        </div>
      </article>
      <!-- 카드 예시 -->

      <!-- JS로 위와 동일한 카드를 생성하여 section#cardSection의 자식으로 추가 -->
    </section>

  </div>

  <script>
    // section#cardSection에 예시와 같은 카드를 생성하여 추가하는 코드를 작성하시오.
    const cardsSection = document.querySelector('#cardsSection')

    function createCard(title, content) {
      const article1 = document.createElement('article')
      article1.setAttribute('class', 'col-4')

      const div1 = document.createElement('div')
      div1.setAttribute('class', 'card m-1')
      article1.append(div1)

      const div2 = document.createElement('div')
      div2.setAttribute('class', 'card-body')
      div1.append(div2)

      const hh5 = document.createElement('h5')
      hh5.setAttribute('class', 'card-title')
      hh5.innerText = title
      div2.append(hh5)

      const pp = document.createElement('p')
      pp.setAttribute('class', 'card-text')
      pp.innerText = content
      div2.append(pp)

      return article1
    } 


    // 카드 생성
    const newCard = createCard('Hello', 'World')

    // DOM에 추가
    cardsSection.appendChild(newCard)

  </script>
</body>

</html>
```

