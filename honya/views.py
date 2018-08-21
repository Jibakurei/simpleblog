from django.shortcuts import render,redirect,get_object_or_404
from .models import ArticleInfo,UserInfo
from .form import ArticleInfoForm,UserInfoForm
from django.http import HttpResponse
from django.template import Template,Context
import json
# Create your views here.
def select(request):
    now = ArticleInfo.objects.all()
    return render(request,'index.html',{'now':now})
    pass

def add(request):
    
    if request.method == "GET":
        return render(request, 'add.html')
    elif request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        bcomment = request.POST['bcomment']
        booklist = ArticleInfo.objects.create(title=title,content=content,bcomment=bcomment)
        #booklist = ArticleInfo.objects.all()

        return redirect('/')






def dels(request,aid):
    a = ArticleInfo.objects.get(id=int(aid))
    a.delete()
    return redirect('/')
    pass

# def edit(request):
#     post = get_object_or_404(ArticleInfo, pk=id)
#     if request.method =="POST":
#         form = ArticleInfoForm(request,ArticleInfo)
#         if form.is_valid():
#             post = form.save(commit=False)
#             #post.author = request.user
#             post.save()
#             return redirect('index',id=ArticleInfo.pk)
#     else:
#         form = ArticleInfoForm(instance=ArticleInfo)
#         return render(request,'book_edit.html',{'form':form})        

def edit(request,aid):
    if request.method == 'GET':
        Articlelist = ArticleInfo.objects.get(id=aid)
        return render(request,'edit.html',{"Articlelist":Articlelist})
    elif request.method =='POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        bcomment = request.POST.get('bcomment')
        ArticleInfo.objects.filter(id=aid).update(title=title,content=content,bcomment=bcomment)
        return redirect('/')

# def funcname(request,aid):
#     if request.method == 'GET':
#         Articlelist = ArticleInfo.objects.get(id=aid)
#         return render(request,'edit.html',{"Articlelist":Articlelist})
#     elif request.method == 'POST':
#         uf = ArticleInfoForm(request.POST)
#         if uf.is_valid():
#             #获得表单数据
#             title = uf.cleaned_data['title']
#             content = uf.cleaned_data['content']
#             bcomment = uf.cleaned_data['bcomment']
#             #添加到数据库
#             ArticleInfo.objects.create(title= title,content=content,bcomment=bcomment)
#             return HttpResponse('Register success!!')
#         else:
#             return HttpResponse('Register failed!!')
#     else:
#         uf = ArticleInfoForm()
#         return render(request, '/', Context({'uf':uf}))


def api(request):
    response = {'code':1000,'data':None}
    response['data'] = [
        {'name':'haiyan','age':22},
        {'name':'haidong','age':10},
        {'name':'haixiyu','age':11},
    ]
    return HttpResponse(json.dumps(response))
    pass

def users(request):
    response = {'code':1000,'data':None}  #code用来表示状态，比如1000代表成功，1001代表
    response['data'] = [
        {'name':'haiyan','age':22},
        {'name':'haidong','age':10},
        {'name':'haixiyu','age':11},
    ]
    return HttpResponse(json.dumps(response))  #返回多条数据

def user(request,pk):
    if request.method =='GET':
        return HttpResponse(json.dumps({'name':'haiyan','age':11}))  #返回一条数据
    elif request.method =='POST':
        return HttpResponse(json.dumps({'code':1111}))  #返回一条数据
    elif request.method =='PUT':
        pass
    elif request.method =='DELETE':
        pass