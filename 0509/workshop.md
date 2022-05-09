```
<template>
  <div>
    <h2 class="text-center">로또</h2>
    <p>{{ lotto }}</p>
    <button @click="getLotto">get lucky numbers</button>

  </div>
</template>

<script>
const _ = require('lodash')
export default {
  name:'lottoView',
  data: function () {
    return {
      lotto: '',
    }
  },
  methods: {
    getLotto: function (){
      const lower = 1
      const upper = 45
      if (this.lotto.length ===0) {
        this.lotto = []
        for (let i=0; i<6; i++){
          this.lotto.push(_.random(lower, upper))
        }
      } else {
        this.lotto = []
        for (let i=0; i<6; i++) {
          this.lotto.push(_.random(lower, upper))
        }
      }
    }
  }

}
</script>

```

```
<template>
  <div>
    <h2 class="text-center">점심메뉴</h2>
    <button @click="getLunch">pick Lunch</button>
    <p>{{ lunchMenu }}</p>
    <h2 class="text-center">로또를뽑아보자</h2>
    <button @click="goLottoPage">pick Lotto</button>
  </div>
</template>

<script>


export default {
  name:'lunchView',
  data: function () {
    return {
      lunchMenus: ['족발', '빵', '계란', '고기'],
      lunchMenu: null,
    }
  },
  methods: {
    goLottoPage: function() {
      this.$router.push({ name: 'lotto' })
    },
    getLunch: function() {
      const idx = Math.floor(Math.random()*this.lunchMenus.length)
      this.lunchMenu = this.lunchMenus[idx]
    }
  }

}
</script>

```

```
import Vue from 'vue'
import VueRouter from 'vue-router'
import lunchView from '../views/lunchView.vue'
import lottoView from '../views/lottoView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/lunch',
    name: 'lunch',
    component: lunchView
  },
  {
    path: '/lotto/6',
    name: 'lotto',
    component: lottoView
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

```

