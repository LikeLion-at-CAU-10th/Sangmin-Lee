# 안쓸거라 지우자.
# from django.shortcuts import render

# ORM 객체 지향적인 방법을 사용하여 데이터베이스의 데이터를 쉽게 조작할 수 있게 해준다. 즉, Django의 ORM은 파이썬과 데이터베이스의 SQL 사이의 통역사 역할을 해준다. SQL 쿼리문 없이도 데이터베이스의 데이터들을 다룰 수 있게되는데, Model Class를 통해서 객체를 만들고 이 객체를 통해서 DB에 접근하는 형식이다.


from django.dispatch import receiver
from footprint.models import Footprint      
from django.http import JsonResponse           # REST한 JSON 응답을 주기 위한 JsonResponse 함수 Import
import json

# Create your views here.

# 팁. 파이썬은 함수 사이 두줄씩 띄어주는 게 컨벤션

# 쟝고는 request 를 매개변수로 받음. 쓰지 않더라도
def footprint_GET(request):

    # 조회 기능
    # orm사용해서 얻은 결과 져쟝
    # -sent_at ; 내림차순 정렬
    # queryset ; 리스트와 비슷한 방식으로 반환
    # 해당 리시버가 들어간 데이터 내림차순으로 정렬해서 저장
    footprints = Footprint.objects.filter(receiver='이상민').order_by('-sent_at')
    messages = []

    # for 문으로 messages 배열안에 추가
    # footprits 에 인덱스값으로 접근하는 이유는 queryset이 리스트와 구조가 비슷하지만 파이썬 기본자료구조가 아니기 때문.
    for i in range(len(footprints)):
        messages.append(footprints[i].message)

    return JsonResponse({
        'status': 200,
        'message': 'Footprint 성공',
        'data': {
            'messages': messages
        }
    })


def footprint_POST(request):
    body_unicode = request.body.decode('utf-8')
    # json 파일 읽어들임. ; 읽어들인  데이터의 값을 취득, 변경, 삭제, 추가하기
    body = json.loads(body_unicode)

    # data 쓸 때 create/ 읽을 때 filter
    Footprint.objects.create(message=body['content'], receiver=body['reveiverName'])

    return JsonResponse({
        'status': 200,
        'message': '메시지 전송 성공'
    })