```
app.vue

<template>
  <div>
    <h2>APP</h2>
      <input type="text" v-model="appdata">
      <p>parentData: {{ parentdata }}</p>
      <p>childData: {{ childdata }}</p>
    
    <AppParent :app="appdata" @parent-data='parentData' @child-data="childData" />
    
    <!-- <AppChild /> -->
  </div>
</template>

<script>
import AppParent from './components/AppParent.vue'


export default {
  name: 'App',
  components: {
   AppParent, 
  },
  data(){
    return {
      appdata: '',
      parentdata: '',
      childdata: '',
    }
  },
  methods: {
   parentData(input) {
      this.parentdata = input
    },
    childData(input) {
      this.childdata = input
    }
  }
}
</script>

<style>

</style>

```

```
appparent.vue

<template>
  <div>
    <h2>APPPARENT</h2>
    <input type="text" @keyup="parentData" v-model="parentdata"> <br>
    <p>appData: {{ app }}</p>
    <p>childData: {{ childdata }}</p>
    
    <AppChild :parent="parentdata" :app="app" @catchParent="catchChild"/>
  </div>
</template>

<script>
import AppChild from './AppChild.vue'

export default {
  name: 'AppParent',
  components :{
    AppChild,
  },
  props: {
    app : String,
  },
  data() {
    return {
      parentdata: '',
      childdata:'',
    }
  },
  methods: {
    parentData() {
      this.$emit('parent-data', this.parentdata)
    },
    catchChild(input) {
      this.childdata = input
      this.$emit('child-data', this.childdata)
    }
  }
} 
</script>

<style>

</style>
```

```
appchild.vue

<template>
  <div>
    <h3>AppChild</h3>
    <input type="text" v-model="childdata" @keyup="throwParent"><br>
    <p>appData: {{ app }} </p>
    <p>parentData: {{ parent }} </p>
    <p>childData: {{ childdata }}</p>
    
  </div>
</template>

<script>
export default {
  name:'AppChild',
  data(){
    return {
      childdata: '',
    }
  },
  props:{
    parent: String,
    app : String,
  },
  methods: {
    throwParent() {
      this.$emit('catchParent', this.childdata)
    }
  }
}
</script>

<style>

</style>
```

