from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
# 함수로 정의하기도 하고 클래스를 쓰기도 한다.
def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')

        data = {
            'name': name
        }
        # context 아니면 바로 딕셔너리로
        return render(request,'index.html', context=data)
    else:
        return render(request, 'index.html')

def http_response(request):
    if request.method == "GET":
        return HttpResponse("Hello WOrld!")


def json_respose(request):
    if request.method == "GET":

        data = {
            'name' : "sm",
            'school' : 'CAU',
        }
        return JsonResponse(data=data)
    
    