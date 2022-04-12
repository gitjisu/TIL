1.  아래의 models.py를 참고하여 User 모델에서 사용할 수 있는 칼럼 중 BooleanField 로 정의 된 컬럼을 모두 작성하시오.

   ```
   is_staff
   is_active
   is_superuser
   ```



2. Django에서 기본적으로 사용하는 User 모델의 username 컬럼이 저장할 수 있는 최대 길이를 작성하시오.

   ```
   max_length=150,
   ```

3. 단순히 사용자가 ‘로그인 된 사용자인지’만을 확인하기 위하여 User 모델 내부에 정의된 속성의 이름을 작성하시오.

```
def is_autentication(self):
or
if request.user.is_authenticated:
```



4. 다음은 로그인 기능을 구현한 코드이다. 빈 칸에 들어갈 코드를 작성하시오

   ```
   a ) AuthenticationForm
   b ) login
   c )	form.get_user()
   ```



5. Who are you?

```
AnonymousUser
```



6. 암호화 알고리즘

```
>>> password = '1234'
>>> hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
>>> hashed_password
b'$2b$12$abMvsZQDKnokMqEGzBHHCu3jVEZIYuY6bheQerYS4E2zDm290/Y7e'

hashed_password = hashed_password.decode('utf-8')
```



7. ```
   로그인 되어 있지 않을때 로그아웃 시도 가능
   ```

   