from django import forms
from .models import User


class SignUpForm(forms.ModelForm):
    password_repeat = forms.CharField(max_length=30,min_length=6)
    def clean(self):
        cleaned_data = super(SignUpForm, self).clean()
        password = cleaned_data.get('password')
        password_repeat = cleaned_data.get('password_repeat')
        if password != password_repeat:
            raise forms.ValidationError(message="两次密码不一致")
        return cleaned_data
    class Meta:
        model = User
        fields = "__all__"

class SignInForm(forms.ModelForm):
    # {'__all__': [{'message': '两次密码不一致', 'code': ''}],
    #  'telephone': [{'message': 'Enter a valid value.', 'code': 'invalid'}]}
    #只想要 两次密码不一致 和  Enter a valid value
    def get_errors(self):
        new_errors = []
        errors = self.errors.get_json_data()
        #dict_values([[{'message': '用户名至少是6位', 'code': 'min_length'}], [{'message': '密码至少是6位', 'code': 'min_length'}]])
        #以上是 errors.values()

        for messages in errors.values():
            for message_dic in messages:
                for key,message in message_dic.items():
                    if key == "message":
                        new_errors.append(message)

        return new_errors

    class Meta:
        model = User
        fields = ['username','password']
        error_messages={
            'username':{
                "min_length":'用户名至少是6位'
            },
            'password':{
                "min_length": '密码至少是6位'
            }
        }

