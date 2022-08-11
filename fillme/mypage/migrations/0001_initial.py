# Generated by Django 4.0.4 on 2022-08-12 00:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=20)),
                ('memo', models.CharField(max_length=100)),
                ('color', models.CharField(blank=True, choices=[('pink', '#FEBCC0'), ('red', '#83333E'), ('lorange', '#FFB37C'), ('orrange', '#FF9A50'), ('yellow', '#FFE886'), ('green', '#153D2E'), ('lblue', '#8692CC'), ('blue', '#486FBB'), ('navy', '#1C0F67'), ('lpurple', '#8878E1'), ('purple', '#4D2E66'), ('etoffe', '#827165'), ('brown', '#231819'), ('gray', '#464648'), ('black', '#010101')], max_length=10, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='mypage/')),
                ('followings', models.ManyToManyField(related_name='followers', to='mypage.profile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('category', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='mypage/')),
                ('openpublic', models.BooleanField(default=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mypage.profile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]