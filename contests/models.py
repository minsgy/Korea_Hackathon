from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from datetime import datetime, date
from users.models import User

# Create your models here.

"""
공모전 모델
"""


class Contest(models.Model):

    # 공모전 이름
    contest_name = models.CharField(max_length=100, null=False)
    # 공모전 주최 기관
    contest_organizer = models.CharField(max_length=100, null=False)
    # 작성자
    author = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="contest_set"
    )
    # 작성 제목
    title = models.CharField(max_length=100, null=False)
    # 마감 기한
    deadline = models.DateField()
    # 공모전 카테고리
    category = models.CharField(max_length=100, null=False)
    # 공모전 포스터
    poster = models.ImageField(upload_to="poster/")
    # 공모전 디테일 - ckeditor
    # detail = RichTextUploadingField()
    detail = models.TextField()
    # 전체 구하는 팀원 수
    # 현재 공모수 조회수
    hit_count = models.PositiveIntegerField(default=0)
    # 언제 생성 했는지 타임라인
    timeline = models.DateTimeField(auto_now_add=True)
    # 마감까지 몇일 남았는지
    days_left = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.contest_name + "/" + self.title

    @property
    def update_hit_counter(self):
        self.hit_count += 1
        self.save()
        return self.hit_count

    @property
    def get_remain_days(self):
        remain_days = (self.deadline - date.today()).days
        self.days_left = remain_days
        self.save()
        return str(remain_days)

    @property
    def get_total_number_of_members(self):
        roles = self.role_set.all()

        total = 0
        for role in roles:
            total += role.max_size

        return total

    def get_number_of_confirmed_members(self):
        roles = self.role_set.all()

        ncm = 0
        for role in roles:
            ncm += role.confirmed_members.count()

        return ncm

    def get_number_of_not_confirmed_members(self):
        roles = self.role_set.all()

        nncm = 0
        for role in roles:
            nncm += role.not_confirmed_members.count()

        return nncm

    def get_TO(self):
        roles = self.role_set.all()

        total = 0
        for role in roles:
            total += role.max_sizes

        ncm = 0
        for role in roles:
            ncm += role.confirmed_members.count()

        return total - ncm

    # 전체 팀원, 남은 모집 인원, 모집중인지 아닌지 함수 해ㅔ야함


"""
공모전 참가자의 역할에 해당하는 모델
"""


class Role(models.Model):

    # 역할 이름
    name = models.CharField(max_length=100, null=False)
    # 최대 인원
    max_size = models.PositiveIntegerField(default=1)
    # 연결된 공모전
    contest = models.ForeignKey(
        "Contest", on_delete=models.CASCADE, related_name="role_set"
    )
    # 수락된 팀원들
    confirmed_members = models.ManyToManyField(
        User, related_name="confirmed_member_set", blank=True
    )
    # 수락 대기중인 사용자들
    not_confirmed_members = models.ManyToManyField(
        User, related_name="not_confirmed_member_set", blank=True
    )

    @property
    def is_full(self):
        return self.confirmed_members.count() == self.max_size
