# Generated by Django 4.0.5 on 2022-08-03 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LikeLion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20, unique=True)),
                ('part', models.CharField(choices=[('기획', '기획'), ('백엔드', '백엔드'), ('프론트엔드', '프론트엔드')], default='백엔드', max_length=20)),
                ('age', models.IntegerField(default=20)),
                ('bio', models.TextField(default='소개를 입력해주세요.', null=True)),
                ('profile_image', models.ImageField(blank=True, max_length=5, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Management',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20)),
                ('age', models.IntegerField(default=20)),
            ],
        ),
    ]
