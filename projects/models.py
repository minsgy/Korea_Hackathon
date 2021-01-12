from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class ProjectTags(models.Model):

    keyword_name = models.CharField(max_length=30) # 프로젝트 키워드 태그
    
    ''' 프로젝트 연결 '''
    projectid = models.ForeignKey(
        "Project", related_name='tags', on_delete=models.CASCADE)


class Project(models.Model):
    ''' 프로젝트 카드 모델 '''
    title = models.CharField(max_length=20)  # 프로젝트 제목
    project_date = models.DateField(null=True)  # 프로젝트 날짜
    position = models.CharField(max_length=40)  # 내 맡은 역할
    description = RichTextUploadingField()  # 프로젝트 설명
    thumnail = models.ImageField(upload_to='images/project_ssumnail/')  # 썸네일

    ''' User 연결 '''
    user = models.ForeignKey( # 유저 모델 연결
        "users.User", related_name="project", on_delete=models.CASCADE)

