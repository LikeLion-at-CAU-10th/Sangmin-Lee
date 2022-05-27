# ORM 객체 지향적인 방법을 사용하여 데이터베이스의 데이터를 쉽게 조작할 수 있게 해준다. 즉, Django의 ORM은 파이썬과 데이터베이스의 SQL 사이의 통역사 역할을 해준다. SQL 쿼리문 없이도 데이터베이스의 데이터들을 다룰 수 있게되는데, Model Class를 통해서 객체를 만들고 이 객체를 통해서 DB에 접근하는 형식이다.

# 아래 두개는 사용하지 않는 모듈.
# from os import major
# from django.dispatch import receiver
# db에서 account 모델에 담긴 정보 가져옴.
from account.models import Account      
from django.http import JsonResponse           # REST한 JSON 응답을 주기 위한 JsonResponse 함수 Import
import json

# 쟝고는 request 를 매개변수로 받음. 쓰지 않더라도

# 데이터 읽어오는 api ; GET은 서버에서 어떤 데이터를 가져와서 보여줄때 사용
def account_GET(request):    
    # nickname 을 기준으로 필터링.(제대로 만든다면 중복되는 거 처리하는 장치가 필요할 듯...)
    accounts = Account.objects.filter(nickname='이상민')
    # 딕셔너리로 넣어줄까?
    # info = {}
    # info['mbti'] = accounts.mbti
    # info['major'] = accounts.major
    # 위 코드 대신 아래코드로 한줄로 간결하게
    info = {'mbti': accounts.mbti, 'major': accounts.major}

    return JsonResponse({
        'status': 200,
        'message': '사용자 정보 조회 성공',
        'data': {
            'information': info
        }
    })

# 데이터 삽입 api ; POST는 서버상의 데이터 값이나 상태를 바꾸기 위해서 사용
def account_POST(request):
    body_unicode = request.body.decode('utf-8')
    # json 파일 읽어들임. ; 읽어들인  데이터의 값을 취득, 변경, 삭제, 추가하기
    body = json.loads(body_unicode)

    # data 쓸 때 create/ 읽을 때 filter
    Account.objects.create( mbti=body['mbti'], major=body['major'])

    # 중복 처리하기 위해 Create 하는 부분에서 filter를 통해 먼저 닉네임을 가진 사용자가 존재하는지 조회, 없다면 유저 생성하는 흐름으로 가야함.

    # 사용자 닉네임이 존재하지않으면 create 가능.
    if Account.objects.filter(nickname='이상민') == False:
        Account.objects.create(nickname=body['name'])

    return JsonResponse({
        'status': 200,
        'message': 'account 데이터 삽입 성공'
    })
