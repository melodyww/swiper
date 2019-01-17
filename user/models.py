from django.db import models


# Create your models here.
class User(models.Model):
    """用户模型"""
    SEX = {
        ("M", "男"),
        ("W", "女")
    }
    phonenu = models.CharField(max_length=16, unique=True, verbose_name="⼿机号")
    nickname = models.CharField(max_length=24, unique=True, verbose_name="昵称")
    sex = models.CharField(max_length=8, choices=SEX, verbose_name="性别")
    birth_year = models.IntegerField(default=2000, verbose_name="出⽣年")
    birth_month = models.IntegerField(default=1, verbose_name="出⽣⽉")
    birth_day = models.IntegerField(default=1, verbose_name="出⽣⽇")
    avatar = models.CharField(max_length=256, verbose_name="个⼈形象URL")
    location = models.CharField(max_length=64, verbose_name="常居地")

    @property
    def profile(self):
        """用户对应的个人设置"""
        if not hasattr(self, "_profile"):
            self._profile, _ = Profile.objects.get_or_create(id=self.id)
        return self._profile


class Profile(models.Model):
    """个人设置"""
    SEX = {
        ("M", "男"),
        ("W", "女")
    }
    location = models.CharField(max_length=20,verbose_name="⽬标城市")
    min_distance = models.IntegerField(default=1, verbose_name="最⼩查找范围")
    max_distance = models.IntegerField(default=10, verbose_name="最⼤查找范围")
    min_dating_age = models.IntegerField(default=18, verbose_name="最⼩交友年龄")
    max_dating_age = models.IntegerField(default=30, verbose_name="最⼤交友年龄")
    dating_sex = models.CharField(max_length=8, choices=SEX, verbose_name="匹配的性别")
    vibration = models.BooleanField(default=True, verbose_name="开启震动")
    only_matche = models.BooleanField(default=True, verbose_name="不让为匹配的⼈看我的相册")
    auto_play = models.BooleanField(default=True, verbose_name="⾃动播放视频")
