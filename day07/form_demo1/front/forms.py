from django import forms
from django.core import validators
from .models import User
#input type=text name='title'
#td 用户名
#td input
class BaseForm(forms.Form):
    #{'telephone': [{'message': '请输入正确格式的手机号', 'code': 'invalid'}], '__all__': [{'message': '两次密码输入不一致', 'code': ''}]}
    #{'telephone':['请输入正确格式的手机号']}
    #1.循环取出 [{'message': '请输入正确格式的手机号', 'code': 'invalid'}]
    #2.取出 message对应的信息   放到新的列表中
    #3.创建空字典 将 最开始的key 作为key  列表作为值  放到新字典中

    def get_errors(self):
        errors = self.errors.get_json_data()
        new_errors = {}
        for key,message_dicts in errors.items():
            # [{'message': '18888888889已经被注册', 'code': ''}]
            messages = []
            for message_dict in message_dicts:
                message = message_dict['message']
                messages.append(message)# ['18888888889已经被注册']
            new_errors[key] = messages

        return new_errors

class MessageBoardForm(BaseForm):
    title = forms.CharField(max_length=100,min_length=6,label="标题",error_messages={"min_length":"最少不能少于6个字符"})
    content = forms.CharField(widget=forms.Textarea,label="内容",error_messages={"required":"内容必填"})
    email = forms.EmailField(label="邮箱",error_messages={"required":"email字段必传"})
    reply = forms.BooleanField(required=False,label="是否回复")

class RegisterForm(BaseForm):
    username = forms.CharField(max_length=100)
    email = forms.CharField(validators=[validators.EmailValidator()])
    telephone = forms.CharField(validators=[validators.RegexValidator(r'1[34578]\d{9}',message="请输入正确格式的手机号")])
    pwd1 = forms.CharField(max_length=20,min_length=6)
    pwd2 = forms.CharField(max_length=20,min_length=6)

    def clean_telephone(self):
        telephone = self.cleaned_data.get('telephone')
        exists = User.objects.filter(telephone=telephone).exists()
        if exists:
            raise forms.ValidationError(message="%s已经被注册" % telephone)
        return telephone

    def clean(self):
        #如果来到了clean方法,说明之前 每一个字段都验证成功了
        cleaned_data = super(RegisterForm, self).clean()
        pwd1 = cleaned_data.get('pwd1')
        pwd2 = cleaned_data.get('pwd2')

        if pwd1!=pwd2:
            raise forms.ValidationError(message="两次密码输入不一致")
        return cleaned_data




