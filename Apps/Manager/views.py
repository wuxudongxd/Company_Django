from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from .forms import RegisterForm
from django.contrib.auth import login as auth_login
from Apps.Manager.models import *
from .serializers import *


@csrf_exempt
def register(request):
    # 从 get 或者 post 请求中获取 next 参数值
    # get 请求中，next 通过 url 传递，即 /?next=value
    # post 请求中，next 通过表单传递，即 <input type="hidden" name="next" value="{{ next }}"/>
    redirect_to = request.POST.get('next', request.GET.get('next', ''))

    # 只有当请求为 POST 时，才表示用户提交了注册信息
    if request.method == 'POST':
        # request.POST 是一个类字典数据结构，记录了用户提交的注册信息
        # 这里提交的就是用户名（username）、密码（password）、邮箱（email）
        # 用这些数据实例化一个用户注册表单
        form = RegisterForm(request.POST)

        # 验证数据的合法性
        if form.is_valid():
            # 如果提交数据合法，调用表单的 save 方法将用户数据保存到数据库
            user = form.save()
            auth_login(request, user, backend='django.contrib.auth.backends.ModelBackend')   # 自动登录

            if redirect_to:
                return redirect(redirect_to)
            else:
                return redirect('/')

            # 注册成功，跳转回首页
            return redirect('/')
    else:
        # 请求不是 POST，表明用户正在访问注册页面，展示一个空的注册表单给用户
        form = RegisterForm()

    # 渲染模板
    # 如果用户正在访问注册页面，则渲染的是一个空的注册表单
    # 如果用户通过表单提交注册信息，但是数据验证不合法，则渲染的是一个带有错误信息的表单
    # 将记录用户注册前页面的 redirect_to 传给模板，以维持 next 参数在整个注册流程中的传递
    return render(request, 'Manager/register.html', context={'form': form, 'next': redirect_to})


def index(request):
    if request.user.is_authenticated:
        if request.user.sign == 'user':
            # 返回简历信息
            resume_list = Resume.objects.filter(author=request.user)
            recruit_list = Recruit.objects.all()
            context = {
                'resume_list': resume_list,
                'recruit_list': recruit_list,
            }
            return render(request, 'Manager/user_detail.html', context)
        elif request.user.sign == 'worker':
            resume_list = Resume.objects.filter(author=request.user)
            department_list = Department.objects.all()
            context = {
                'resume_list': resume_list,
                'department_list': department_list,
            }
            return render(request, 'Manager/worker_detail.html', context)
        elif request.user.sign == 'superuser':
            users_list = User.objects.all()
            resume_list = Resume.objects.filter(author=request.user)
            department_list = Department.objects.all()
            position_list = Position.objects.all()
            context = {
                'users_list': users_list,
                'resume_list': resume_list,
                'department_list': department_list,
                'position_list': position_list,
            }
            return render(request, 'Manager/admin_detail.html', context)
    return render(request, 'index.html')


# 用户
class UserList(generics.ListAPIView, generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers


class UserDetail(generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers


# 部门
class DepartmentList(generics.ListAPIView, generics.CreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializers


class DepartmentDetail(generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializers


# 职位
class PositionList(generics.ListAPIView, generics.CreateAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializers


class PositionDetail(generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializers


# 招聘
class RecruitList(generics.ListAPIView, generics.CreateAPIView):
    queryset = Recruit.objects.all()
    serializer_class = RecruitSerializers


class RecruitDetail(generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Recruit.objects.all()
    serializer_class = RecruitSerializers


# 简历
class ResumeList(generics.ListAPIView, generics.CreateAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializers


class ResumeDetail(generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializers
