1. ```
   1) T
   2) T
   3) T
   ```

2. ```
   call stack에 console.log('hello ssafy')
   output에 hello ssafy -> call stack 비움
   setTimeout이 call stack에 들어오고 web API로 요청을 보내고 3초를 기다린다
   call stack에 cosole.log('bye SSAFY') 
   output에 bye SSAFY -> call stack 비워짐
   3초 후 Task Queue에 setimeout -> call stack -> console.log('I am from setTimeout')
   ```

   