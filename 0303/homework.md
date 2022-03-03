1. ```
   LANGUAGE_CODE = 'ko-kr'
   ```

2. ```
   'ssafy/', views.ssafy
   ```

3. ```
   {% for menu in menus%}
   	<p>{{ menu }}</p>
   {% endfor %}
   ```

4. ```
   forloop.counter0
   ```

5. ```
   empty
   ```

6. ```
   for
   forloop.last
   ```

7. ````
   a =
   b = title
   ````

8. ```
   Y m d D A h i
   ```

9. ```
   action - 어디로 보내면 되는지 적는 곳이다. 요청을 처리할 url을 적는다.
   ```

10. ```
    GET = URL뒤에 파라미터를 붙여 전송, 노출위험
    POST = 데이터 전송량에 제한 x 대용량 데이터 o 노출위험x
    ```

11. ```
    /create/안녕하세요/반갑습니다/파이팅
    ```