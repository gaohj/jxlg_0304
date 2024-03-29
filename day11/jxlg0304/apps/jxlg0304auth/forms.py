#encoding:utf-8
from django import forms
from apps.forms import FormMixin
from .models import User
from django.core import validators
from django.core.cache import cache

class LoginForm(forms.Form,FormMixin):
    telephone = forms.CharField(max_length=11,validators=[validators.RegexValidator(r'1[3456789]\d{9}',message="请输入正确格式的手机号")])
    password = forms.CharField(max_length=30,min_length=6,error_messages={"max_length":"密码最长不过30位","min_length":"密码最短不能少于6位"})
    remember = forms.IntegerField(required=False)


class RegisterForm(forms.Form,FormMixin):
    telephone = forms.CharField(max_length=11,validators=[validators.RegexValidator(r'1[3456789]\d{9}',message="请输入正确格式的手机号")])
    username = forms.CharField(max_length=100)
    password1 = forms.CharField(max_length=30, min_length=6,
                               error_messages={"max_length": "密码最长不过30位", "min_length": "密码最短不能少于6位"})
    password2 = forms.CharField(max_length=30, min_length=6,
                               error_messages={"max_length": "密码最长不过30位", "min_length": "密码最短不能少于6位"})
    img_captcha = forms.CharField(max_length=4,min_length=4)
    sms_captcha = forms.CharField(max_length=4,min_length=4)

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 != password2:
            forms.ValidationError("两次密码输入不一致")

        img_captcha = cleaned_data.get('img_captcha')
        cached_img_captcha = cache.get(img_captcha.lower())

        if not cached_img_captcha or cached_img_captcha.lower() != img_captcha.lower():
            raise forms.ValidationError("图形验证码错误")

        sms_captcha = cleaned_data.get('sms_captcha')
        cached_sms_captcha = cache.get(sms_captcha.lower())
        if not cached_sms_captcha or cached_sms_captcha.lower() != sms_captcha.lower():
            raise forms.ValidationError("图形验证码错误")

        telephone = cleaned_data.get('telephone')
        exists = User.objects.filter(telephone=telephone).exists()
        if exists:
            forms.ValidationError("该手机号码已经注册")
        return cleaned_data