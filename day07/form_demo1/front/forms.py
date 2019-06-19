from django import forms
#input type=text name='title'
#td 用户名
#td input
class MessageBoardForm(forms.Form):
    title = forms.CharField(max_length=100,min_length=6,label="标题",error_messages={"min_length":"最少不能少于6个字符"})
    content = forms.CharField(widget=forms.Textarea,label="内容",error_messages={"required":"内容必填"})
    email = forms.EmailField(label="邮箱",error_messages={"required":"email字段必传"})
    reply = forms.BooleanField(required=False,label="是否回复")

