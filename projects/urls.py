from django.urls import path
from . import views

''' 포트폴리오 프로젝트 생성/수정 및 디테일 페이지 URL'''
urlpatterns = [
    # 프로젝트 생성/수정 및 프로젝트 상세 페이지
    path('project_create/', views.project_create, name='project_create'), # 생성
    path('project_update/<int:pk>', views.project_update, name='project_update'), # 수정
    path('project_delete/<int:pk>', views.project_delete, name='project_delete'), # 수정
    path('project_detail/<int:pk>', views.project_detail, name='project_detail'), # 상세
]