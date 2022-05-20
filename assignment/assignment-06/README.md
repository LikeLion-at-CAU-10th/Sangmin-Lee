# session-06 Django 서버구축

manage.py가 있는 폴더에서 django-admin startapp footprint 명령어를 터미널에 입력
; footprint라는 app 실행

django project 설정파일인 settings.py로 가서 INSTALLED_APPS에 footprint 넣어주기.

django 기본 url인 http://127.0.0.1:8000/ 뒤에 뭐가 붙는지에 따라 어디로 가는지 길안내하는 역할.
예를 들어 뒤에 footprint/ 가 붙어서 http://127.0.0.1:8000/footprint/ 이면 footprint 폴더의 urls.py로 넘어가고
http://127.0.0.1:8000/footprint/ ; views.py에 있는 footprint_GET 함수실행
http://127.0.0.1:8000/footprint/send ; views.py에 있는 footprint_POST 함수실행

footprint_GET / footprint_POST 함수 정의.

models.py 에서는 Database Model을 정의한다. ; 받을 데이터를 정의하는 부분
AutoField 메서드는 자동으로 숫자하나 증가해서 식별하는 데 좋다. DB설계할 때 유용

터미널에 python manage.py makemigrations 와 python manage.py migrate 명령어를 순차적으로 실행.
