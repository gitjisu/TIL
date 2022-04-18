1. ```
   1) T
   2) T
   3) F 반드시는 아니지만 설정하는것을 권장
   ```

2. ```
   (a) : user
   (b) : article.like_user.all
   ```

3. ````
   (a): user_pk
   (b): followers
   (c): filter
   (d): remove
   (e): add
   ````

4. ```
   기존의 User모델을 참조하고 있기 때문이다.
   settings_AUTH_USER_MODEL을 변경했기 때문에
   from django_contrib.auth import get_user_model
   User = get_user_model()
   ```

5. ```
   네이밍만 보고도 관계유추가 가능
   ```

   