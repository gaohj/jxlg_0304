from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager,AbstractBaseUser, PermissionsMixin
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
# Create your models here.

# class Person(User):
#
#     class Meta:
#         proxy = True
#
#     @classmethod
#     def get_blacklist(cls):
#         return cls.objects.filter(is_active=False)

# class UserExtension(models.Model):
#     user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="extension")
#     telephone = models.CharField(max_length=11)
#     school = models.CharField(max_length=100)
#
#
# @receiver(post_save,sender=User)
# def handle_user_extension(sender,instance,created,**kwargs):
#     if created: #如果是新建
#         UserExtension.objects.create(user=instance)
#     else: #这是更新
#         instance.extension.save()

class UserManager(BaseUserManager):
    def _create_user(self, telephone,username, email, password, **kwargs):
        if not telephone:
            raise ValueError('必须要传手机号')
        if not password:
            raise ValueError('必须要传密码')
        user = self.model( telephone=telephone,username=username,email=email,password=password,**kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, telephone,username, email, password, **kwargs):
        kwargs['is_superuser'] = False
        return self._create_user(telephone=telephone,username=username,email=email,password=password,**kwargs)

    def create_superuser(self,telephone,username, email, password, **kwargs):
        kwargs['is_superuser'] = True
        return self._create_user(telephone=telephone, username=username, email=email, password=password,**kwargs)

# class User(AbstractUser):
#     telephone = models.CharField(max_length=11,unique=True)
#     school = models.CharField(max_length=30)
#
#     objects = UserManager()
#
#     USERNAME_FIELD = 'telephone'
class User(AbstractBaseUser, PermissionsMixin):
    telephone = models.CharField(max_length=11, unique=True)
    email = models.EmailField(max_length=100,unique=True)
    username = models.CharField(max_length=100,unique=True)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'telephone'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)

    class Meta:
        permissions = [
            ('view_article','查看文章的权限')
        ]



