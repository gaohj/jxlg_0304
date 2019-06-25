from django import forms

from django.contrib.auth import get_user_model
#跟 from .models import User 效果是一样的


class LoginForm(forms.ModelForm):
    remember = forms.IntegerField(required=False)
    telephone = forms.CharField(max_length=11)

    class Meta:
        model = get_user_model()
        fields = ['password']
