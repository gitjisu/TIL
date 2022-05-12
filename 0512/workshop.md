```
App.vue

<template>
  <div id="app">
    <h1>TodoList</h1>
    <h4>전체 Todo {{ allTodosCount }}개</h4>
    <h4>완료한 Todo {{ completedTodosCount }} 개</h4>
    <h4>남은 Todo {{ unCompletedTodosCount }}개</h4>
    <hr>
    <TodoForm />
    
    <TodoList />
  </div>
</template>

<script>
import TodoForm from '@/components/TodoForm.vue'
import TodoList from '@/components/TodoList.vue'
import {mapGetters} from 'vuex'


export default {
  name: 'App',
  components: {
    TodoForm, TodoList
  },
  computed: {
    ...mapGetters([
      'allTodosCount',
      'completedTodosCount',
      'unCompletedTodosCount'
    ])
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

```

```
TodoForm.vue

<template>
  <div>
    <h4>할 일 만들기</h4>
    <input type="text" v-model.trim="todoTitle">
    <button @click="createTodo">ADD</button>
  </div>
</template>

<script>
export default {
  name:'TodoForm',
  data() {
    return {
      todoTitle: '',
    }
  },
  methods: {
    // Todo 객체 {} 생성
    createTodo() {
      const todoItem = {
        title: this.todoTitle,
        isCompleted: false,
        date: new Date().getTime() 
      }
    // todo 객체의 생성
    if (todoItem.title) {
      // dispatch = actions으로 쏘는 것
      // 첫번째인자 actions에 있는 함수 이름
      // 두번째인자 payload
      this.$store.dispatch('createTodo', todoItem)
    }
    // 데이터 비워주기
    this.todoTitle = ''
    }
  }
}
</script>

<style>

</style>
```

```
TodoList.vue

<template>
  <div>
    <!-- {{ $store.state.todos }} store에서 직접 가져올 수 있지만 사용하지 x -->
    <TodoListItem v-for="todo in todos" :key="todo.data" :todo="todo" />
  </div>
</template>

<script>
import TodoListItem from '@/components/TodoListItem.vue'


export default {
  name:'TodoList',
  components: {
    TodoListItem,
  },
  computed: {
    todos() {
      return this.$store.state.todos
    }
  }

}
</script>

<style>

</style>
```

```
TodolistItem.vue

<template>
  <div>
    <!-- isCompleted가 참이되는 경우 is-completed가 on -->
    <span @click="updateTodo(todo)" :class="{'is-completed' : todo.isCompleted}" class="todo-cursor">
      {{ todo.title }}
      <!-- <button @click="deleteTodo">삭제</button> -->
      <!-- deleteTodo(todo)는 실행하는게 아님, todo를 payload로 넘기겠다는 말 -->
      <button @click="deleteTodo(todo)">삭제</button>
    </span>
  </div>
</template>

<script>
import {mapActions} from 'vuex'

export default {
  name: 'TodoListItem',
  props: {
    todo: Object,
  },
  methods: {
    // 삭제하는 메서드 : 버튼 눌렀을때
    // deleteTodo(){
    //   // this.todo === props에서 넘어온 todo
    //   this.$store.dispatch('deleteTodo', this.todo)
    // },
    // update 메서드 : span태그 눌렀을때
    // updateTodo(){
    //   this.$store.dispatch('updateTodo', this.todo)
    // }
    // map을 사용할때 payload를 어떻게 보낼꺼? 
    ...mapActions([
      'deleteTodo',
      'updateTodo'
    ])

  }
}
</script>

<style scoped>
  .is-completed {
    text-decoration: line-through;
  }

  .todo-cursor {
    cursor: pointer;
  }
</style>
```

