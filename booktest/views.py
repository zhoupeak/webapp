from django.shortcuts import render,redirect
from booktest.models import BookInfo
from datetime import date

from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.

def index(request):
    ''' 显示图书馆信息'''

    books = BookInfo.objects.all()
    #2.使用模板
    return  render(request, 'booktest/index.html',{'books':books})

def create(request):
    '''新增一本图书'''
    print('-----------------------------------------------')
    # 1.创建BookInfo对象
    b = BookInfo()
    b.btitle = '流星蝴蝶剑'
    b.bpub_date = date(1990,1,1)
    # 2.保存进数据库
    b.save()
    # 3.返回应答,让浏览器再访问/index,重定向
    # return HttpResponse('ok')
    return HttpResponseRedirect('/tushu/index')
    # return redirect('/index/index')




def delete(request,bid):
    book= BookInfo.objects.get(id=bid)
    book.delete()
    # return  HttpResponsePermanentRedirect('/index/index')
    print('-----------------------------------------------')
    return redirect('/tushu/index')


