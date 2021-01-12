from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateProject
from .models import Project, ProjectTags
from django.core.exceptions import PermissionDenied

# 포트폴리오 프로젝트 Create 
def project_create(request):

    if request.method == "POST":
        # 프로젝트 생성하기
        s1 = request.POST.get('description').split("media/") # 썸네일 분리
        s2 = s1[1].split('"')
        project = Project(
            title=request.POST.get('title'),
            project_date=request.POST.get('project_date'),
            position=request.POST.get('position'),
            description=request.POST.get('description'),
            user=request.user,
            thumnail=s2[0]
        )
        project.save()
        # 태그 생성하기
        tags = request.POST.get('project_tags').split(',')
        for tag in tags:
            tg = ProjectTags(
                keyword_name=tag,
                projectid=project
            )
            tg.save() # 키워드 태그 생성
        return redirect('portfolio_detail', request.user.pk)

    else:
        form = CreateProject()
        return render(request, 'project_create.html', {"form":form})

# 유저 프로젝트 Update 
def project_update(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        # 프로젝트 생성하기
        s1 = request.POST.get('description').split("media/") # 썸네일 분리
        s2 = s1[1].split('"')

        project.title = request.POST.get('title')
        project.project_date = request.POST.get('project_date')
        project.position=request.POST.get('position')
        project.description=request.POST.get('description')
        project.user=request.user
        project.thumnail=s2[0]
        
        project.save()
        # 태그 생성하기 
        tag = project.tags.all()
        tag.delete()

        tags = request.POST.get('project_tags').split(',')
        for tag in tags:
            tg = ProjectTags(
                keyword_name=tag,
                projectid=project
            )
            tg.save() # 키워드 태그 생성
        return redirect('portfolio_detail', request.user.pk)

    else:
        form = CreateProject(instance=project)
        return render(request, 'project_update.html', {"form": form, "project":project})

# 유저 프로젝트 delete
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.user == project.user:
        project.delete()
        return redirect('portfolio_detail', request.user.pk)
    raise PermissionDenied

# 유저 프로젝트 디테일 페이지
def project_detail(request, pk):    
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'project_detail.html', {"project":project})
