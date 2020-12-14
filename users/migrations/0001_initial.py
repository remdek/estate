# Generated by Django 3.1.3 on 2020-12-14 04:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('attach', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(blank=True, default=None, max_length=254, null=True, unique=True, verbose_name='Email')),
                ('phone', models.DecimalField(blank=True, decimal_places=0, max_digits=11, null=True, verbose_name='Телефон')),
                ('block', models.BooleanField(default=False, verbose_name='Active')),
                ('block_description', models.TextField(blank=True, verbose_name='Blocking reason')),
                ('password', models.CharField(blank=True, max_length=128, verbose_name='Password')),
                ('first_name', models.CharField(max_length=50, verbose_name='First name')),
                ('last_name', models.CharField(blank=True, max_length=50, verbose_name='Last Name')),
                ('position', models.CharField(blank=True, max_length=100, verbose_name='Должность')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('birth', models.DateField(blank=True, null=True, verbose_name='Date birth')),
                ('uid', models.CharField(blank=True, max_length=20, verbose_name='User ID')),
                ('address', models.CharField(blank=True, max_length=250, verbose_name='Address')),
                ('card', models.DecimalField(blank=True, decimal_places=0, max_digits=16, null=True, verbose_name='Номер карты')),
                ('last_ip', models.CharField(blank=True, max_length=20, verbose_name='Last IP')),
                ('confirm', models.CharField(blank=True, max_length=32, null=True, verbose_name='Код подтверждения')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создана')),
                ('updated', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Обновлена')),
                ('avatar', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_avatar', to='attach.image', verbose_name='Avatar')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Contact Name')),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
            },
        ),
        migrations.CreateModel(
            name='UserContacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=200, verbose_name='Value')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userContacts_contact', to='users.contacts', verbose_name='Contact')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userContacts_user', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'UserContact',
                'verbose_name_plural': 'UsersContacts',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Groups')),
                ('parent', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='group_parent', to='users.group')),
            ],
            options={
                'verbose_name': 'Group',
                'verbose_name_plural': 'Groups',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='contacts',
            field=models.ManyToManyField(blank=True, related_name='user_contacts', through='users.UserContacts', to='users.Contacts'),
        ),
        migrations.AddField(
            model_name='user',
            name='group',
            field=models.ManyToManyField(related_name='user_group', to='users.Group', verbose_name='Group'),
        ),
    ]
