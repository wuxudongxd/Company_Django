from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy

from .models import *


class UserProfileAdmin(UserAdmin):
    list_display = ['username', 'last_login', 'is_superuser', 'is_staff', 'is_active', 'date_joined']
    fieldsets = (
        (None, {'fields': ('username', 'password', 'first_name', 'last_name', 'email')}),

        (gettext_lazy('用户信息'), {'fields': ('nickname', 'gender', 'sign', 'age', 'job_number', 'payment')}),

        (gettext_lazy('Permissions'), {'fields': ('is_superuser', 'is_staff', 'is_active',
                                                  'groups', 'user_permissions')}),

        (gettext_lazy('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'site', 'persons', 'leader',]
    fields = ['name', 'site', 'persons', 'leader']


class PositionAdmin(admin.ModelAdmin):
    list_display = ['name']
    fields = ['name']


class RecruitAdmin(admin.ModelAdmin):
    list_display = ['author', 'recruit_num']
    fields = ['author', 'department', 'recruit_num', 'position', 'text']


class ResumeAdmin(admin.ModelAdmin):
    list_display = ['author']
    fields = ['text', 'recruit']

    # 自动保存作者名
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)


admin.site.register(User, UserProfileAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(Recruit, RecruitAdmin)
admin.site.register(Resume, ResumeAdmin)

