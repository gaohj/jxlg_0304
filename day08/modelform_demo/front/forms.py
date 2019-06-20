from django import forms
from .models import Book,User
class MyForm(forms.Form):
    # username = forms.URLField(max_length=4)

    def get_errors(self):
        errors = self.errors.get_json_data()
        new_errors = {}
        for key,message_dicts in errors.items():
            messages = []
            #message_dicts
			#[{'message':'1'}]
            #[{'message':'2'}]
            for message in message_dicts:
                messages.append(message['message'])
            new_errors[key] = messages
        return new_errors

class AddBookForm(forms.ModelForm,MyForm):
    def clean_page(self):
        page = self.cleaned_data.get('page')
        if page > 100:
            raise forms.ValidationError("页数不能大于100")
        return page
    class Meta:
        model = Book
        fields = "__all__"
        # fields = ['title','page']
        # exclude = ['price']
        error_messages = {
            'page':{
                'required':'请传入page参数',
                'invalid':'请传入一个可用的page参数'
            },
            'title':{
                'max_length':'title不能超过100个字符'
            },
            'price':{
                'max_value':"图书价格不能超过1000元"
            }
        }


class RegisterForm(forms.ModelForm):
    pwd1 = forms.CharField(max_length=30,min_length=6)
    pwd2 = forms.CharField(max_length=30,min_length=6)

    #走到这里说明所有的字段都验证成功了

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        pwd1 = self.cleaned_data.get('pwd1')
        pwd2 = self.cleaned_data.get('pwd2')
        if pwd1 != pwd2:
            raise forms.ValidationError("两次密码输入不一致")
        return cleaned_data
    class Meta:
        model = User
        exclude = ['password']