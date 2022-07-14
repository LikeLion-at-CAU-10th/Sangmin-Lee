import json
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import *

def create_category(requests):

    if requests.method == "POST":

        # 디코드를 반드시
        body = json.loads(requests.body.decode('utf-8'))
    
        # create로 정보 입력
        new_category = Category.objects.create(
            title = body['title'],
            view_auth = body['view_auth'],
            color = body['color']
        )
        # json 형태로 예쁘게 만들기
        new_category_json = {
            'id' : new_category.id,
            'title' : new_category.title,
            'view_auth' : new_category.view_auth,
            'color' : new_category.color,
        }
        return JsonResponse({
            'status': 200,  #성공
            'success' : True,
            'message': '생성 성공',
            'data': new_category_json

        })

    else:
        return JsonResponse({
            'status': 405,  #실패
            'success' : False,
            'message': '생성 실패',
            'data': None
        })


# 2번째 api
def get_category_all(requests):
    if requests.method == "GET":

        # 객체 전부를 가져옴. 대신 주의해야할 건 Queryset 형태로 받아온다는 거. -> 가져다 쓰려면 for문 돌려서 넣어야지.   
        category_all = Category.objects.all()

        category_json_all = []

        for category in category_all:
            # json형태로 예쁘게 정리하고.
            category_json = {
                'id' : category.id,
                'title' : category.title,
                'view_auth' : category.view_auth,
                'color' : category.color,
            }
            # 전체 json이 담기도록 리스트에 append ; 리스트에 딕셔너리형태의 json 파일들이 들어있는 형태.
            category_json_all.append(category_json)

        return JsonResponse({
            'status': 200,  #성공
            'success' : True,
            'message': '생성 성공',
            'data': category_json_all

        })

    else:
        return JsonResponse({
            'status': 405,  #실패
            'success' : False,
            'message': '생성 실패',
            'data': None
        })    

# 특정 pk값을 받아와야하기 때문에 함수의 매개변수에 적어줘야함!!!
def get_category(requests, id):
    if requests.method == "GET":
        # create한 걸 받아오려면 인덱스pk 필요
        # 하나만 가져올 때 get_object_or_404 사용 ; pk 값만 받아옴. ;; url 보낼 때 id도 같이 보내주도록 작성.
        category = get_object_or_404(Category, pk =id)

        category_json = {
            'id' : category.id,
            'title' : category.title,
            'view_auth' : category.view_auth,
            'color' : category.color,
        }
        return JsonResponse({
            'status': 200,  #성공
            'success' : True,
            'message': '생성 성공',
            'data': category_json

        })

    else:
        return JsonResponse({
            'status': 405,  #실패
            'success' : False,
            'message': '생성 실패',
            'data': None
        })

# category_id 는 urls.py에서 받아온 매개변수
def create_todo(request, category_id):
    if request.method == 'POST':

    # 이미지는 다르게 받는데
        body = request.POST
        # 이해 필요
        img = request.FILES['thumb_nail']
    
        new_todo = Todo.objects.create(
            # 주의. 모델생성시에는 따옴표써주고 Create 해줄때는 따옴표없이 모델을 불러옴.
            category = get_object_or_404(Category, pk=category_id),
            content = body['content'],
            thumb_nail = img
        )
    
        new_todo_json = {
                'id' : new_todo.id,
                'content' : new_todo.content,
                'thumb_nail' : '/media/' + str(new_todo.thumb_nail),
                'is_completed' : new_todo.is_completed,
                'pub_date' :new_todo.pub_date,
    
            }
    
        return JsonResponse({
            'status': 200,  #성공
            'success' : True,
            'message': '생성 성공',
            'data': new_todo_json

        })

    else:
        return JsonResponse({
            'status': 405,  #실패
            'success' : False,
            'message': '생성 실패',
            'data': None
        })   

    # 이미지도 gitignore에 포함. 장고에서 알아서해주느 ㄴ것 같음.