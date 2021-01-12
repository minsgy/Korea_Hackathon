# [민석] : 유저 모델 및 관련 모델 생성

from django.db import models
from django.contrib.auth.models import AbstractUser
from django_fields import DefaultStaticImageField


class HashTags(models.Model):
    """ 자기 소개용 해시태그 Model """

    tag_name = models.CharField(max_length=20)  # 해시태그이름
    user = models.ForeignKey(  # User 외래키
        "users.User", related_name="hashtags", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.tag_name


class User(AbstractUser):

    """ 연결된 모델 """

    # HashTags 1:N
    # Contest N:M

    # 구현해야 할 목록
    # 뱃지 이벤트들 구현해야함 ..

    """ 사용자 + 포트폴리오 모델  """
    name = models.CharField(max_length=20)  # 이름
    image = DefaultStaticImageField(upload_to="images/", blank=True)  # 프로필 사진
    phone_number = models.CharField(max_length=20)  # 전화번호
    email = models.CharField(max_length=30)  # 이메일

    major = models.CharField(max_length=20)  # 전공
    university = models.CharField(max_length=40)  # 학교
    description = models.CharField(max_length=40)  # 한 마디
    hit_count = models.PositiveIntegerField(default=0)  # 조회수 계산값

    def __str__(self):
        return self.name

    # 유저에 대한 포트폴리오 조회수 카운트 반환
    @property
    def update_hitcount(self):
        self.hit_count = self.hit_count + 1
        self.save()
        return self.hit_count
