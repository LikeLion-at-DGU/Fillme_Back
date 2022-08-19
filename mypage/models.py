from tkinter.tix import Tree
from unicodedata import category
from django.db import models
from django.dispatch import receiver
from accounts.models import User
from django.db.models.signals import post_save
from notice.serializers import *

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=20)
    memo = models.CharField(max_length=100)
    COLOR_LIST = (
        ('pink', '#FEBCC0'),
        ('red', '#83333E'),
        ('lorange', '#FFB37C'),
        ('orrange', '#FF9A50'),
        ('yellow', '#FFE886'),
        ('green', '#153D2E'),
        ('lblue', '#8692CC'),
        ('blue', '#486FBB'),
        ('navy', '#1C0F67'),
        ('lpurple', '#8878E1'),
        ('purple', '#4D2E66'),
        ('etoffe', '#827165'),
        ('brown', '#231819'),
        ('gray', '#464648'),
        ('black', '#010101'),
    )
    color = models.CharField(max_length=10, choices=COLOR_LIST, blank=True, null=True)
    ## 프론트에서 가져올때 : profile.color 는 키값, profile.get_color_display() 는 내용
    image = models.ImageField(upload_to = "mypage/", blank=True, null=True)
    followings = models.ManyToManyField("self", related_name="followers", symmetrical=False)
    subfollowings = models.ManyToManyField("Persona", related_name="subfollowers", symmetrical=False)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if User.objects.filter(username = "youngseo").exists():
        base1 = User.objects.filter(username = "youngseo")[0]
        instance.profile.followings.add(base1.profile)
        follower_subs1 = base1.persona_set.all()
        for i in range(base1.persona_set.all().count()):
            instance.profile.subfollowings.add(follower_subs1[i])
        notice1 = NoticeSerializer(data={
            "user":base1.id,
            "userfrom":instance.username,
            "userto":"회원",
            "text":"님을 팔로우하기 시작했습니다.",
            "content":"null"
        })
        if notice1.is_valid():
            notice1.save()
    if User.objects.filter(username = "yaena1223").exists():
        base2 = User.objects.filter(username = "yaena1223")[0]
        instance.profile.followings.add(base2.profile)
        follower_subs2 = base2.persona_set.all()
        for i in range(base2.persona_set.all().count()):
            instance.profile.subfollowings.add(follower_subs2[i])
        notice2 = NoticeSerializer(data={
            "user":base2.id,
            "userfrom":instance.username,
            "userto":"회원",
            "text":"님을 팔로우하기 시작했습니다.",
            "content":"null"
        })
        if notice2.is_valid():
            notice2.save()
    if User.objects.filter(username = "asher").exists():
        base3 = User.objects.filter(username = "asher")[0]
        instance.profile.followings.add(base3.profile)
        follower_subs3 = base3.persona_set.all()
        for i in range(base3.persona_set.all().count()):
            instance.profile.subfollowings.add(follower_subs3[i])
        notice3 = NoticeSerializer(data={
            "user":base3.id,
            "userfrom":instance.username,
            "userto":"회원",
            "text":"님을 팔로우하기 시작했습니다.",
            "content":"null"
        })
        if notice3.is_valid():
            notice3.save()
    if User.objects.filter(username = "dudtlstm").exists():
        base4 = User.objects.filter(username = "dudtlstm")[0]
        instance.profile.followings.add(base4.profile)
        follower_subs4 = base4.persona_set.all()
        for i in range(base4.persona_set.all().count()):
            instance.profile.subfollowings.add(follower_subs4[i])
        notice4 = NoticeSerializer(data={
            "user":base4.id,
            "userfrom":instance.username,
            "userto":"회원",
            "text":"님을 팔로우하기 시작했습니다.",
            "content":"null"
        })
        if notice4.is_valid():
            notice4.save()
    if User.objects.filter(username = "yoons02").exists():
        base5 = User.objects.filter(username = "yoons02")[0]
        instance.profile.followings.add(base5.profile)
        follower_subs5 = base5.persona_set.all()
        for i in range(base5.persona_set.all().count()):
            instance.profile.subfollowings.add(follower_subs5[i])
        notice5 = NoticeSerializer(data={
            "user":base5.id,
            "userfrom":instance.username,
            "userto":"회원",
            "text":"님을 팔로우하기 시작했습니다.",
            "content":"null"
        })
        if notice5.is_valid():
            notice5.save()
    if User.objects.filter(username = "zoonong").exists():
        base6 = User.objects.filter(username = "zoonong")[0]
        instance.profile.followings.add(base6.profile)
        follower_subs6 = base6.persona_set.all()
        for i in range(base6.persona_set.all().count()):
            instance.profile.subfollowings.add(follower_subs6[i])
        notice6 = NoticeSerializer(data={
            "user":base6.id,
            "userfrom":instance.username,
            "userto":"회원",
            "text":"님을 팔로우하기 시작했습니다.",
            "content":"null"
        })
        if notice6.is_valid():
            notice6.save()
    instance.profile.save()


class Persona(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    profile = models.ForeignKey(Profile, related_name='personas', on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    category = models.CharField(max_length=100)
    image = models.ImageField(upload_to = "mypage/", blank=True, null=True)
    openpublic = models.BooleanField(default=True)