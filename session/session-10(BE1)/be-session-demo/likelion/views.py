from django.shortcuts import render

from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView
from .models import LikeLion
# Create your views here.

class LikeLionCreateview(CreateView):
    model = LikeLion
    fields = "__all__"
    success_url = '/likelion'

# 전체 조회
class LikeLionListView(ListView):
    model = LikeLion
    # 페이지네이션 ; 몇개씩 끊을 건지.
    paginate_by = 30
    ordering = ['name']

class LikeLionUpdateView(UpdateView):
    model = LikeLion
    fields = "__all__"
    # 이해필요
    template_name_suffix = "_update_form"
    success_url = '/likelion'

class LikeLionDeleteView(DeleteView):
    model = LikeLion
    success_url = '/likelion'
