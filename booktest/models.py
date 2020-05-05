from django.db import models

# Create your models here.

class BookInfo(models.Model):
    '''图书模型类'''
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateField()
    # 阅读量
    bread = models.IntegerField(default=0)
    #评论量
    bcomment = models.IntegerField(default=0)
    #删除标记
    isDelete = models.BooleanField(default=False)

# 多类 关系属性
class HeroInfo(models.Model):
    '''英雄人物类型'''
    #英雄名称
    hname  = models.CharField(max_length=20)

    # 性别
    hgender = models.BooleanField(default=False)
    # 备注
    hcomment = models.CharField(max_length=200)

    hbook = models.ForeignKey('BookInfo',on_delete=models.CASCADE,)

    isDelete = models.BooleanField(default=False)