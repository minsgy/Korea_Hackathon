from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import auth

# CBV import
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator
from django.views.generic.list import ListView

# Model Import
from .models import User, HashTags


def portfolio_searching(request) :

    ''' Product Searching fbv '''

    users = User.objects.all()
    if request.GET.get:
        search = request.GET.get('search')
        print("검색어 확인",search, type(search))
        
        users = User.objects.all().filter(name__icontains = search)

        return render(request, 'search_portfolio.html',{"users" : users})
    
    return render(request, 'portfolio_list.html',{"users" : users})

# 포트폴리오 리스트 페이지
class portfolio_list(ListView):
    '''포트폴리오(유저) 디테일'''
    model = User
    paginate_by = 9
    context_object_name = 'users'
    template_name = 'portfolio_list.html'

# 유저 포트폴리오 페이지
class portfolio_detail(DetailView):
    '''포트폴리오(유저) 디테일'''
    model = User
    context_object_name = 'users'
    template_name = 'portfolio_detail.html' 

# 포트폴리오 내정보 수정 페이지
def user_edit(request):
    users = request.user
    if request.method == 'POST':
        users.phone_number = request.POST['phone_number']
        users.email = request.POST['email']
        users.description = request.POST['description']
       
        tag = users.hashtags.all()
        tag.delete()

        tags = request.POST.get('tags').split(',')
        for tg in tags:
            g = HashTags(
                tag_name=tg,
                user=users
            )
            g.save() # 키워드 태그 생성
        
        return redirect('portfolio_detail', request.user.pk)
    

    return render(request, 'user_editor.html', {"users":users})



# -------------------------------------------------
''' User Model '''

# User Login View
def user_login(request):
    # POST 형식의 로그인 폼 값 전달 시에 함수 실행
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # 입력한 username과 password 가 서버에 있는 회원인지 확인하는 함수.
        # 이 결과 (회원이다. 아니다.) 를 user 에 넣어준다.
        # 찾아서 id, paasword 일치하는 지 확인
        user = auth.authenticate(request, username=username, password=password)

        # 로그인 됐을 시 none이 아니기 때문에, 메인으로 이동해야함!
        if user is not None:
            auth.login(request, user)
            return redirect('main') # 메인으로 이동해야함.

        # 로그인 안됐을 시, 오류 안내
        else:
            print("로그인 실패")
            return redirect('user_login')
   
    #Login Form으로 이동 할 시 기본 로그인 창으로 이동함.
    else:
        return render(request, "user_login.html")

# 유저 로그아웃
def user_logout(request):
    auth.logout(request)
    return redirect('main')


# 유저
def user_signup(request):
    # 유저 회원가입 폼 정상 작성시
    if request.method == 'POST':
        if request.POST.get('password1') == request.POST.get('password2'):
            user_ = User.objects.create_user(
                username=request.POST.get('username'), 
                password=request.POST.get('password1'), 
                #image = request.FILES['image'],
                name=request.POST.get('name'),
                email=request.POST.get('email'),
                phone_number=request.POST.get('phone_number'),
                major=request.POST.get('major'),
                university=request.POST.get('university'),
                description=request.POST.get('description'),
            )
            if 'image' in request.FILES:
                user_.image = request.FILES['image']

            user_.save()
            hashtags = request.POST.get('hashtags').split(',')
            for hstag in hashtags:
                hashtag = HashTags(
                    tag_name=hstag,
                    user=user_
                )
                hashtag.save()
                
            auth.login(request, user_)
            return redirect('main')
        print("생성안됌.")
        return redirect('user_signup')
    else:
        return render(request, 'user_signup.html')
    return redirect('user_signup')