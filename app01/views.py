from django.shortcuts import render

# Create your views here.
from django import forms
class LoginForm(forms.Form):    #定义规则
    user = forms.CharField(required=True)
    pwd = forms.CharField(required=True)


def login(request):
    if request.method == 'POST':
        obj = LoginForm(request.POST)
        ret = obj.is_valid()    # 判断获得用户的数据是否符合规则
        #print(ret)
        if ret:
            print(obj.clean())      # 如果不为空则获取用户数据
        else:
            print(obj.errors)       # 如果为空则返回相应的错误信息

        # u = request.POST.get('user')
        # p = request.POST.get('user')
        # print(u,p)
    return render(request,'login.html')