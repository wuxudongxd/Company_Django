from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):
    nickname = models.CharField('昵称', max_length=50, blank=True)
    gender = models.CharField('性别', max_length=10, choices=(('male', '男'), ('female', '女'), ('no', '未知')), default='no')
    sign = models.CharField('权限', max_length=10, choices=(('user', '用户'), ('worker', '员工'), ('superuser', '管理员')), default='user')
    age = models.IntegerField('年龄', blank=True, null=True)
    email = models.EmailField('邮箱', unique=True)
    job_number = models.IntegerField('工号', blank=True, null=True)
    payment = models.IntegerField('薪酬', blank=True, null=True)

    class Meta(AbstractUser.Meta):
        verbose_name = '用户'
        verbose_name_plural = verbose_name


class Department(models.Model):
    name = models.CharField('部门名称', max_length=50, unique=True)
    site = models.CharField('部门位置', max_length=50, blank=True)
    persons = models.IntegerField('部门人数', blank=True, null=True)
    leader = models.CharField('部门领导', max_length=50, blank=True)
    created_time = models.DateTimeField('创建时间', default=timezone.now)

    class Meta:
        verbose_name = '部门'
        verbose_name_plural = verbose_name


class Position(models.Model):
    name = models.CharField('职位名称', max_length=50)
    created_time = models.DateTimeField('创建时间', default=timezone.now)

    class Meta:
        verbose_name = '职位'
        verbose_name_plural = verbose_name


class Recruit(models.Model):
    author = models.ForeignKey(User, verbose_name='发布者', on_delete=models.CASCADE)
    department = models.ManyToManyField(Department, verbose_name='招聘部门', blank=True)
    recruit_num = models.IntegerField('招聘人数', blank=True, null=True)
    position = models.ManyToManyField(Position, verbose_name='招聘职位', blank=True)
    text = models.TextField('招聘内容', blank=True)
    created_time = models.DateTimeField('创建时间', default=timezone.now)

    class Meta:
        verbose_name = '招聘'
        verbose_name_plural = verbose_name


class Resume(models.Model):
    author = models.ForeignKey(User, verbose_name='用户', on_delete=models.CASCADE)
    text = models.TextField('简历内容', blank=True)
    recruit = models.ForeignKey(Recruit, verbose_name='招聘信息', on_delete=models.CASCADE)
    created_time = models.DateTimeField('创建时间', default=timezone.now)

    class Meta:
        verbose_name = '简历'
        verbose_name_plural = verbose_name
