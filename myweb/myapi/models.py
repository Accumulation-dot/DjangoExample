from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

from django.utils.html import format_html




"""
class User(AbstractUser):
    u_id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False,
                            verbose_name='model id', help_text='唯一的id')
    role = models.CharField(max_length=10, default='user',
                            choices=(('user', '普通用户'), ('admin', '管理员'), ('vip', 'VIP')))

    @property
    def is_active(self):
        return self.role == 'admin'

    @property
    def is_staff(self):
        return self.role == 'admin'

    def has_perm(self, *args, **kwargs):
        return self.role == 'admin'

    def has_module_perms(self, *args, **kwargs):
        return self.role == 'admin'

    def __str__(self):
        return self.u_id

    class Meta:
        db_table = 'auth_user'
        verbose_name = '用户表'
        verbose_name_plural = verbose_name


class Account(UUIDModel):
    ACCOUNT_TYPE = (
        (1, '账号密码'),
        (2, '手机密码'),
        (3, '邮箱'),
        (4, '手机验证码'),
        (5, '微信'),
        (6, '微博')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             verbose_name='用户', help_text='用户信息')
    type = models.PositiveSmallIntegerField(choices=ACCOUNT_TYPE, default=1,
                                            verbose_name='账号类型', help_text='登陆类型')
    name = models.CharField(max_length=40, unique=True,
                            verbose_name='账号信息', help_text='账号的信息，记录手机号码、邮箱、账号、微博号、微信号')
    secure = models.CharField(max_length=60, blank=True, default='',
                              verbose_name='安全信息', help_text='保存关于密码方面的信息, 微信微博第三方登陆可能为空')
    other = models.CharField(max_length=60, default='', null=True, blank=True,
                             verbose_name='其它', help_text='记录其它可用信息')

    def __str__(self):
        return self.type.value_to_string()

    class Meta:
        verbose_name = '登陆'
        verbose_name_plural = verbose_name

    def save_with(self, user):
        self.user = user
        self.save()


class UserInformation(UUIDModel):
    GENDER_TYPE = (
        (0, '男'),
        (1, '女'),
        (2, '默认'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=60, blank=True, default='')
    age = models.PositiveSmallIntegerField(blank=True, default=0)
    gender = models.PositiveSmallIntegerField(choices=GENDER_TYPE, default=2,
                                              verbose_name='性别', help_text='性别的选项 从GENDER_TYPE中选取 默认为2')
    vip = models.PositiveSmallIntegerField(default=0, verbose_name='vip等级', help_text='记录vip等级')

    class Meta:
        verbose_name = '用户信息表'
        verbose_name_plural = verbose_name

    def save_with(self, user):
        self.user = user
        self.save()


class UserProfile(UUIDModel):
    DEVICE_TYPE = (
        (-1, 'unknown'),
        (0, 'web'),
        (1, 'ios'),
        (2, 'android'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    device = models.SmallIntegerField(choices=DEVICE_TYPE, default=-1)
    ip = models.GenericIPAddressField(default='0.0.0.0', blank=True, null=True)

    class Meta:
        verbose_name = '登陆信息表'
        verbose_name_plural = verbose_name

    def save_with(self, user, request):
        self.user = user
        if request.META.get('HTTP_X_FORWARDED_FOR'):
            ip = request.META.get("HTTP_X_FORWARDED_FOR")
        else:
            ip = request.META.get("REMOTE_ADDR")
        self.ip = ip
        self.device = 1
        self.save()
"""
