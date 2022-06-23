from unicodedata import name
from django.shortcuts import render

# Create your views here.

def home(request):
    if request.method =="POST":
        name = request.POST.get('name')
        return render(request, 'index.html', {"name": name})
    else:
        return render(request, 'index.html')
