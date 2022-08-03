from django.contrib import admin
from .models import LikeLion

# Register your models here.

# 어드민 커스텀
@admin.register(LikeLion)
class LikeLionModelAdmin(admin.ModelAdmin):

    # list_display = ('id', 'name', 'part', )
    # 정렬 기준
    # list_filter = ('part')

    # search_fields = 
    # 뭐 기준으로 검색할지 설명
    # serch_help_text =
    # 못 수정하게 막아놓을 수도
    # readonly_fields: Sequence[str]

    list_display =  ('id', 'name', 'part', 'age', 'bio', 'profile_image',)
    list_editable = ('bio',)
    list_filter = ('part',)
    search_fields = ('id', 'name', 'part')
    search_help_text = ''