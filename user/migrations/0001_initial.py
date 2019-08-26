# Generated by Django 2.0 on 2019-08-14 02:51

from django.db import migrations, models
import user.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgentOrSaleManOrOperate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('account', models.CharField(blank=True, max_length=32, null=True, verbose_name='用户邮箱')),
                ('mobile', models.CharField(max_length=11, unique=True, verbose_name='联系手机号')),
                ('name', models.CharField(blank=True, max_length=32, null=True, verbose_name='联系人姓名')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '代理商或者销售代表或者运营表',
                'verbose_name_plural': '代理商或者销售代表或者运营表',
                'db_table': 'agent_saleman_operate',
            },
            managers=[
                ('objects', user.models.UserManager()),
            ],
        ),
    ]
