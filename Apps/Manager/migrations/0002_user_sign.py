# Generated by Django 3.0.2 on 2020-01-14 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='sign',
            field=models.CharField(choices=[('user', '用户'), ('worker', '员工'), ('superuser', '管理员')], default='user', max_length=10, verbose_name='权限'),
        ),
    ]
