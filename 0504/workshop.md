```
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Lunch & Lotto</title>
</head>

<body>
  <div id="app">
    <h2>점심메뉴</h2>
    <button @click="getlunch">Pick One</button>
    <p>{{ selectedLunch }}</p>
    <hr>

    <h2>로또</h2>
    <button @click="getnum">Get Lucky Numbers</button>
    <p>{{ lotto }}</p>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/lodash.js/4.17.20/lodash.min.js"></script>
  <script>
    const app = new Vue({
      el: '#app',
      data: {
        lunch : ['국밥', '짜장면', '라면', '과일'],
        selectedLunch : '',
        lotto: []
      },
      methods: {
        getlunch: function () {
          const idx = Math.floor(Math.random() * this.lunch.length)
          this.selectedLunch = this.lunch[idx]
        },
        getnum: function () {
          const lower = 1
          const upper = 45
          for (let i=0; i<6; i++){
            this.lotto.push(_.random(lower, upper))
          }
        }
      }
    })
  </script>
</body>

</html>
```

