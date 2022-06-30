from django.shortcuts import render, get_object_or_404
import json
from django.http import JsonResponse
from .models import Profile

# profile Create api
def create_profile(requests):

    if requests.method == "POST":
        # 디코딩 ; DB에 올려줄 때는 디코딩해서 올려준다.
        body = json.loads(requests.body.decode('utf-8'))

        # Profile모델에서 객체,틀 생성
        new_profile = Profile.objects.create(
            name = body['name'],
            age = body['age'],
            phone = body['phone'],

        )

        # json으로 예쁘게 보자
        profile_json = {
            'id' : new_profile.id,
            'name' : new_profile.name,
            'age' : new_profile.age,
            'phone' : new_profile.phone,

        }
        # 성공시 response
        return JsonResponse({
            'status': 200,  #성공
            'success' : True,
            'message': 'Create 성공',
            'data': profile_json

        })
    else:
        # 실패시 response
        return JsonResponse({
            'status': 405,  #실패
            'success' : False,
            'message': 'Create 실패',
            'data': None
        })

# db에 담긴 모든 profile 객체 Read 하는 api
def get_profiles_all(requests):

    if requests.method == "GET":

        # 객체 전부 가져옴.; QuerySet 형태로
        profiles_all = Profile.objects.all()
        
        # 객체들이 담길 리스트
        profiles_all_json = []

        # for문으로 객체별로 json형태로 정리
        for profile in profiles_all:
            profile_json = {
                'id': profile.id,
                'name': profile.name,
                'age': profile.age,
                'phone': profile.phone,

            }
            profiles_all_json.append(profile_json)


        return JsonResponse({
            'status': 200,  #성공
            'success' : True,
            'message': 'Read 성공',
            'data': profiles_all_json

        })

    else:
        return JsonResponse({
            'status': 405,  #실패
            'success' : False,
            'message': 'Read 실패',
            'data': None
        })    


# 특정 id값을 갖는 profile만 Read 하는 api
def get_profile(requests, id):
    
    if requests.method == "GET":
        profile = get_object_or_404(Profile, pk=id)

        profile_json = {
            'id': profile.id,
            'name': profile.name,
            'age': profile.age,
            'phone': profile.phone,
        }

        return JsonResponse({
            'status': 200,  #성공
            'success' : True,
            'message': 'Read 성공',
            'data': profile_json

        })

    else:
        return JsonResponse({
            'status': 405,  #실패
            'success' : False,
            'message': 'Read 실패',
            'data': None
        })    


def update_profile(requests, id):
    if requests.method == "PATCH":

        body = json.loads(requests.body.decode('utf-8'))

        # 특정 pk값에 해당하는 객체 가져오기.
        update_profile = get_object_or_404(Profile, pk=id)
        
        # 그 객체의 각각의 값 Update
        update_profile.name = body['name']
        update_profile.age = body['age']
        update_profile.phone = body['phone']

        update_profile_json = {
            # id는 위에서 업데이트 안했으니 그대로.
            'id': update_profile.id,
            'name': update_profile.name,
            'age': update_profile.age,
            'phone': update_profile.phone,

        }
        return JsonResponse({
            'status': 200,  #성공
            'success' : True,
            'message': 'Update 성공',
            'data': update_profile_json

        })

    else:
        return JsonResponse({
            'status': 405,  #실패
            'success' : False,
            'message': 'Update 실패',
            'data': None
        })


def delete_profile(requests, id):
    if requests.method =="DELETE":
        delete_profile = get_object_or_404(Profile, pk=id)
        # 특정 profile Delete
        delete_profile.delete()

        return JsonResponse({
                'status': 200,
                'success': True,
                'message': 'Delete 성공!',
                'data': None
            })
    else:
        return JsonResponse({
                'status': 405,
                'success': False,
                'message': 'Delete error',
                'data': None
            })

