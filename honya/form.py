from django import forms
from .models import ArticleInfo,UserInfo

class ArticleInfoForm(forms.ModelForm):
    class mete:
        model = ArticleInfo
        fields = ('title','content','bcomment'),
        pass
    pass
class UserInfoForm(forms.ModelForm):
    class mete:
        model = UserInfo
        fields = ('username','password','email',),
        pass
    pass