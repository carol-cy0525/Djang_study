from django import http
from django.db.models import F,Q,Sum
from django.views import View
from django.shortcuts import render
from mysqltest.models import BookInfo,HeroInfo

# Create your views here.



class ORMTest(View):
    def get(self,request):
        # book = BookInfo.objects.filter(id__gt=1)
        # for b in book:
        #     print(b.bread)
        book = BookInfo.objects.get(id=1)
        a = book.bread
        print(a)

        # # 关联查询 一到多 多到一
        # book = BookInfo.objects.get(id=1)
        # b = book.heroinfo_set.all()
        # print(b)
        #
        # h = HeroInfo.objects.get(id=1)
        # name = h.hname
        # print(name)

        # # 排序 order_by()
        # book = BookInfo.objects.filter().order_by('bread')
        # print(book)
        # book = BookInfo.objects.filter().order_by('-bread')
        # print(book)

        # # 聚合函数 Sum()
        # book = BookInfo.objects.aggregate(Sum('bread'))
        # print(book)

        # # Q查询
        # book = BookInfo.objects.filter(Q(bread__gt=30) | Q(id__gt=3))
        # print(book)
        # book = BookInfo.objects.filter(~Q(id__gt=3))
        # print(book)

        # # F查询
        # book = BookInfo.objects.filter(bread__gt=F('bcomment'))
        # print(book)

        # 过滤查询  语法：模型类对象 = 模型类名.objects.filter(属性名__条件表达式=值)
        # book = BookInfo.objects.filter(属性名__条件表达式=值)
        # print(book)

        # 相等 exact=============================================
        # book = BookInfo.objects.filter(id__exact=1)
        # # book = BookInfo.objects.filter(id=1) # 简写
        # print(book)

        # # 不相等 exclude()=======================================
        # book = BookInfo.objects.exclude(id=3)
        # print(book)

        # # 4,查 基本查询 get()单一结果  all()所有结果  count()================
        # count = BookInfo.objects.count()
        # print(count)


        # # 3,删 delete()  或者 ================================
        # book = BookInfo.objects.get(id=7)
        # book.delete()
        #
        # BookInfo.objects.filter(id=6).delete()


        # # 2,改 save() 或者 update()===========================
        # book = BookInfo.objects.get(id=5)
        # book.btitle='谁动了我的奶酪'
        # book.save()
        #
        # BookInfo.objects.filter(id=6).update(btitle='西游记')


        # # 1,增 save() 或者 create()==========================
        # book = BookInfo()
        # book.btitle = '自传'
        # book.bpub_date = '2020-5-20'
        # book.bread = 20
        # book.bcomment = 30
        # book.save()
        #
        # BookInfo.objects.create(
        #     btitle='游记',
        #     bpub_date='2020-5-21',
        #     bread=30,
        #     bcomment=50
        # )


        return http.HttpResponse('数据库增删改查')








