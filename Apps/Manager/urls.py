from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter  # 导入

router = DefaultRouter()  # 实例化router

router.register('users', views.UserList)

app_name = 'Manager'
urlpatterns = [
    path('', include(router.urls)),
    # path('users/', views.UserList.as_view(), name='UserList'),
    # path('users/<int:pk>/', views.UserDetail.as_view(), name='UserDetail'),
    path('departments/', views.DepartmentList.as_view(), name='DepartmentList'),
    path('departments/<int:pk>/', views.DepartmentDetail.as_view(), name='DepartmentDetail'),
    path('positions/', views.PositionList.as_view(), name='PositionList'),
    path('positions/<int:pk>/', views.PositionDetail.as_view(), name='PositionDetail'),
    path('recruits/', views.RecruitList.as_view(), name='RecruitList'),
    path('recruits/<int:pk>/', views.RecruitDetail.as_view(), name='RecruitDetail'),
    path('resumes/', views.ResumeList.as_view(), name='ResumeList'),
    path('resumes/<int:pk>/', views.ResumeDetail.as_view(), name='ResumeDetail'),
]
