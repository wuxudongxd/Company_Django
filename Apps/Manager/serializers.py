from rest_framework import serializers
from . import models


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ("username", "password", "nickname", "sign", "gender", "age", "email", "job_number", "payment")


class DepartmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Department
        fields = ("name", "site", "persons", "leader")


class PositionSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Position
        fields = ("name", "created_time")


class RecruitSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Recruit
        fields = ("author", "department", "recruit_num", "position", "text", "created_time")


class ResumeSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Resume
        fields = ("author", "text", "recruit", "created_time")
