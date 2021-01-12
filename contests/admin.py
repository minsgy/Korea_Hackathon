from django.contrib import admin
from .models import Contest, Role

# Register your models here.
admin.site.register(Contest)


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):

    list_display = ("name", "contest")

    filter_horizontal = ("confirmed_members", "not_confirmed_members")
