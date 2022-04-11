1.Django 에서 기본적으로 사용하는 User모델은 아래의 경로에서 찾아볼 수 있다.

아래의 Django 공식 github에서 user모델이 정의된 코드를 찾아 작성하시오.

```
from django.contrib.auth.models import User
```

```
class User(AbstractUser):
    """
    Users within the Django authentication system are represented by this
    model.
    Username and password are required. Other fields are optional.
    """

    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"
```



2. Create user by ModelForm 새 유저를 생성하는 django 내부에 정의된 ModelForm을 사용하기 위한 import구문을 작성하시오

```
from django.contrib.auth.forms import AuthenticationForm
```



3. Django sessions 

```
a) 장고
b) session_key
```

