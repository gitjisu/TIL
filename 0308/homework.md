1. django가 model에 생긴 변화를 db에 반영하는 방법 = migration



2. 변경사항 저장하기
   - 위에서 작성한 model의 변경사항을 저장하기 위한 명령어를 작성하시오.
     - python manage.py makemigrations
   - 이로 인해 생성된 마이그레이션 파일에 대응되는 SQL문을 확인하기 위한 명령어와 출력결과를 작성하기오(app의 이름은 articles이다)
     - python manage.py sqlmigrate articles 0001
3.  python shell
   - django에서 사용 가능한 모듈 및 메서드를 대화식 python shell 에서 사용하려고 할 때, 어떤 명령어를 통해 해당 shell을 실행할 수 있는지 작성하시오.
     - python manage.py shell_plus
4. Django Model Field
   - django에서 model을 정의할 때 사용할 수 있는 필드 타입을 5가지 이상 작성하시오
     - TextField DateField DateTimeField FloatField CharField