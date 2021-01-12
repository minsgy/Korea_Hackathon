from django.shortcuts import render, redirect, HttpResponse
from .models import Contest, Role
from users.models import User
from django.views.decorators.http import require_POST
import json
from .remind_module import sms_reminder

# Create your views here.

"""
공모전 생성
입력값을 불러와 새로운 공모전 모델 생성
"""


def create_contest(request):

    if request.user.is_authenticated:
        current_user = request.user
    else:
        return redirect("user_login")

    if request.method == "POST":

        # 새로운 객체 생성
        new_contest = Contest()

        # 템플릿으로부터 데이터를 불러오는 코드
        new_contest.author = current_user
        new_contest.contest_name = request.POST["contest_name"]
        new_contest.contest_organizer = request.POST["contest_organizer"]
        new_contest.title = request.POST["title"]
        new_contest.deadline = request.POST["deadline"]
        new_contest.category = request.POST["category"]
        new_contest.detail = request.POST["detail"]
        new_contest.poster = request.FILES["poster"]

        new_contest.save()

        # request.POST => csrt_token + 공모전 입력값들 + 역할 개수
        number_of_roles = int((len(request.POST) - 6) / 2)

        print(number_of_roles)

        for i in range(number_of_roles):

            new_role = Role()

            new_role.contest = new_contest

            name_index = "role_name_" + str(i)
            new_role.name = request.POST[name_index]
            size_index = "role_size_" + str(i)
            new_role.max_size = int(request.POST[size_index])
            new_role.save()

        return redirect("contest_list")

    return render(request, "contest_create.html")


"""
공모전의 리스트를 불러오는 함수
검색 기능, 키워드 별로 정렬 해주는 기능 필요
"""

# 정렬, 검색 둘다 한번에 할 수 있으면 최고 , 안되면 어쩔 수 없음
def display_contest_list(request):

    if request.user.is_authenticated:
        current_user = request.user
    else:
        return redirect("user_login")

    if "my_post" in request.POST:
        contests = current_user.contest_set.all()
        return render(request, "contest_list.html", {"contests": contests})

    # search bar 구현
    if "search" in request.GET:
        search_keyword = request.GET["search"]
        print(search_keyword)
        filtered_contests = Contest.objects.filter(
            contest_name__contains=search_keyword
        )
        print(len(filtered_contests))
        context = {"contests": filtered_contests}
        return render(request, "contest_list.html", context)

    # 기본 정렬 기준 : 생성 시간
    contest_query_set = Contest.objects.order_by("timeline")

    if "sort" in request.GET:
        if request.GET.get("sort") == "hit":
            keyword = "hit_count"
        elif request.GET.get("sort") == "days":
            keyword = "days_left"
        else:
            keyword = "timeline"

        contest_query_set = Contest.objects.order_by(keyword)

    context = {"contests": contest_query_set}

    return render(request, "contest_list.html", context)


"""
불러온 공모전 데이터를 삭제하는 함수
"""


def delete_contest(request, contest_id):

    contest = Contest.objects.get(pk=contest_id)
    contest.delete()
    return redirect("contest_list")


"""
공모전의 디테일을 보여주는 함수
"""


def display_contest_detail(request, contest_id):

    # 로그인이 안돼있을 경우 로그인 페이지로 이동
    if not request.user.is_authenticated:
        # 로그인 페이지로 바꿔줘야함
        return redirect("user_login")
    else:
        current_user = request.user

    current_user = request.user

    contest = Contest.objects.get(pk=contest_id)

    if current_user.id == contest.author.id:
        access = True
    else:
        access = False

    context = {
        "contest": contest,
        "access": access,
    }

    # 신청 한 사람은 신청 못하게 해야 하는데 이건 어떻게 처리하지 ?

    return render(request, "contest_detail.html", context)


"""
공모전 수정 페이지
"""


def update_contest(request, contest_id):

    contest = Contest.objects.get(pk=contest_id)
    roles = contest.role_set.all()

    if request.method == "POST":
        contest.contest_name = request.POST["contest_name"]
        contest.contest_organizer = request.POST["contest_organizer"]
        contest.title = request.POST["title"]
        contest.deadline = request.POST["deadline"]
        contest.category = request.POST["category"]

        contest.save()

        # request.POST => csrt_token + 공모전 입력값들 + 역할 개수
        number_of_roles = int((len(request.POST) - 6) / 2)

        print(number_of_roles)

        for i in range(number_of_roles):

            size_index = "role_size_" + str(i)
            name_index = "role_name_" + str(i)

            if i > len(roles):
                new_role = Role()

                new_role.contest = contest

                new_role.name = request.POST[name_index]
                new_role.max_size = int(request.POST[size_index])
                new_role.save()
                continue

            if roles[i].name == request.POST[name_index] and roles[i].max_size == int(
                request.POST[size_index]
            ):
                continue

            else:
                roles[i].name = request.POST[name_index]
                roles[i].max_size = int(request.POST[size_index])
                roles[i].save()

        return redirect("contest_detail", contest_id)

    return render(request, "contest_update.html", {"contest": contest})


def register_into_team(request, role_id, contest_id):

    role = Role.objects.get(pk=role_id)
    user = request.user

    role.not_confirmed_members.add(user)

    contest = Contest.objects.get(pk=contest_id)
    print(user)
    print(contest.author, contest.author.id)

    sms_reminder('register', user.id, contest.author.id)

    return redirect("contest_detail", contest_id)


"""
신청한 사람을 팀원으로 뽑아가는 함수
"""


@require_POST
def register_in_team(request):
    contest_id = request.POST["contest_id"]
    role_id = request.POST["role_id"]
    user_id = request.POST["user_id"]

    print(contest_id + role_id + user_id)

    role = Role.objects.get(pk=role_id)
    user = User.objects.get(pk=user_id)

    if role.confirmed_members.count() >= role.max_size:
        message = "fail"
    else:
        role.confirmed_members.add(user)
        role.not_confirmed_members.remove(user)
        message = "connect success"

    # ajax를 이용한 비동기 통신을 위한 코드
    context = {
        "message": message,
        "role_name": role.name,
        "role_max_size": role.max_size,
        "user_name": user.name,
        "major": user.major,
    }

    sms_reminder('confirm', request.user.id, user.id)

    return HttpResponse(json.dumps(context), content_type="application/json")


@require_POST
def deny(request):
    contest_id = request.POST["contest_id"]
    role_id = request.POST["role_id"]
    user_id = request.POST["user_id"]

    print(contest_id + role_id + user_id)

    role = Role.objects.get(pk=role_id)
    user = User.objects.get(pk=user_id)

    role.not_confirmed_members.remove(user)

    context = {
        "username": user.name,
    }

    return HttpResponse(json.dumps(context), content_type="application/json")


@require_POST
def expulsion(request):
    contest_id = request.POST["contest_id"]
    role_id = request.POST["role_id"]
    user_id = request.POST["user_id"]

    print(contest_id + role_id + user_id)

    role = Role.objects.get(pk=role_id)
    user = User.objects.get(pk=user_id)

    role.confirmed_members.remove(user)

    context = {
        "username": user.name,
        "rolename": role.name,
        "major": user.major,
    }

    return HttpResponse(json.dumps(context), content_type="application/json")