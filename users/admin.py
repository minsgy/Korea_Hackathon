from django.contrib import admin
from .models import User, HashTags
from django.contrib.auth.admin import UserAdmin

# Register your models here.

# Hash Tags 어드민 페이지 생성
admin.site.register(HashTags)

# 유저 커스텀 모델로 인해 자체 어드민 페이지 생성
@admin.register(User)
class CustomUserAdmin(UserAdmin):

    ''' User admin Custom '''

    fieldsets = (
        (None, {"fields": ("username", "password", "name", "image",
                           "phone_number", "email", "major", "university", "description")},),
    )

    list_display = (
        "username",
        "name",
        "image",
        "email",
        "phone_number",
        "major",
        "university",
        "description",
    )
