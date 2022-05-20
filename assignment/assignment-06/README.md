# session-06 Django 서버구축

manage.py가 있는 폴더에서 django-admin startapp footprint 명령어를 터미널에 입력
; footprint라는 app 실행

![스크린샷 2022-05-19 오후 10 09 20](https://user-images.githubusercontent.com/101850881/169530309-1694f58c-662c-487b-ad12-b2542fd8ef05.png)

<br>
django project 설정파일인 settings.py로 가서 INSTALLED_APPS에 footprint 넣어주기.

![스크린샷 2022-05-19 오후 10 43 55](https://user-images.githubusercontent.com/101850881/169530398-96a89cd3-d3da-424b-a1e5-e905251beec9.png)


django 기본 url인 http://127.0.0.1:8000/ 뒤에 뭐가 붙는지에 따라 어디로 가는지 길안내하는 역할.

예를 들어 뒤에 footprint/ 가 붙어서 http://127.0.0.1:8000/footprint/ 이면 footprint 폴더의 urls.py로 넘어가고

http://127.0.0.1:8000/footprint/ ; views.py에 있는 footprint_GET 함수실행
http://127.0.0.1:8000/footprint/send ; views.py에 있는 footprint_POST 함수실행

![스크린샷 2022-05-20 오후 9 43 53](https://user-images.githubusercontent.com/101850881/169530655-da6c7287-534e-4052-aa8e-e3b51a3ba490.png)

![스크린샷 2022-05-20 오후 9 44 14](https://user-images.githubusercontent.com/101850881/169530678-ec991701-fe47-4559-908d-2f8042ff8c92.png)


footprint_GET / footprint_POST 함수 정의.

![스크린샷 2022-05-20 오후 9 46 07](https://user-images.githubusercontent.com/101850881/169530972-8244a08f-ac58-4d4c-8e0f-404e18fc3a3e.png)

![스크린샷 2022-05-20 오후 9 46 16](https://user-images.githubusercontent.com/101850881/169530998-22544bd7-1695-4de7-8b8f-fbf7af416155.png)


models.py 에서는 Database Model을 정의한다. ; 받을 데이터를 정의하는 부분
AutoField 메서드는 자동으로 +1씩 증가해서 식별하는 데 좋다. DB설계할 때 유용

![스크린샷 2022-05-19 오후 11 15 24](https://user-images.githubusercontent.com/101850881/169531124-ee6f85fe-61b0-4078-97c5-15e6c580a02b.png)

터미널에 python manage.py makemigrations 와 python manage.py migrate 명령어를 순차적으로 실행.
python manage.py makemigrations ; 마이그레이션 생성
python manage.py migrate ; 생성한 마이그레이션을 DB에 적용

![스크린샷 2022-05-19 오후 11 40 16](https://user-images.githubusercontent.com/101850881/169531186-816ccd26-14ab-4b55-8d81-86735799f0a7.png)
