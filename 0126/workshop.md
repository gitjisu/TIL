```
fake data가 필요할때 faker라이브러리를 사용할 수 있음
터미널에서 실행
```

```
from faker import Faker #라이브러리 임폴트를 위한 코드이다
fake = Faker() #Faker는 class, fake는 인스턴스이다
fake.name #name()은 fake의 메서드이다.
```

```
def __init__(self, name)
```

```
seed = 랜덤 추출시 샘플링 결과가 실행할 때 마다 고정된 값을 얻을 수 있게 해줌
#1 shelly wilcox
#2 박진우
```

```
seed_instance = 공유된 인스턴스와 분리된 자체 인스턴스로 변환
#1 shelly wilcox
#2 박진우
```

