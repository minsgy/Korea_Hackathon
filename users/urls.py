from django.urls import path
from . import views

urlpatterns = [
    # 유저 로그인/로그아웃/회원가입
    path('user_editor/', views.user_edit ,name="user_editor"),
    path('user_login/', views.user_login ,name="user_login"),
    path('user_logout/', views.user_logout, name="user_logout"),
    path('user_signup/', views.user_signup, name="user_signup"),
    path('portfolio_detail/<int:pk>', views.portfolio_detail.as_view(), name="portfolio_detail"),  # 유저 포트폴리오 개인 페이지 이동
    path('portfolio/', views.portfolio_list.as_view(),name="portfolio_list"),  # 유저 포트폴리오 리스트
    path('portfolio_search/', views.portfolio_searching,name="search_list"),  # 유저 포트폴리오 리스트
]