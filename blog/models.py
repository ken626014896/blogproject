from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Post(models.Model)    :


    title=models.CharField(max_length=70)

    body=models.TextField()

    created_time=models.DateTimeField()
    modified_time=models.DateTimeField()#最后修改时间


    excerpt=models.CharField(max_length=200,blank=True)#文章摘要

    #我们规定一篇文章只能对应一个分类，但是一个分类下可以有多篇文章，所以我们使用的是
    #ForeignKey，即一对多的关联关系。
    # 而对于标签来说，一篇文章可以有多个标签，同一个标签下也可能有多篇文章，所以我们使用 ManyToManyField，表明这是多对多的关联关系。
    # 同时我们规定文章可以没有标签，因此为标签 tags 指定了 blank=True。
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    tags=models.ManyToManyField(Tag,blank=True)

    # 文章作者，这里 User 是从 django.contrib.auth.models 导入的。
    # django.contrib.auth 是 Django 内置的应用，专门用于处理网站用户的注册、登录等流程，User 是 Django 为我们已经写好的用户模型。
    # 这里我们通过 ForeignKey 把文章和 User 关联了起来。
    # 因为我们规定一篇文章只能有一个作者，而一个作者可能会写多篇文章，因此这是一对多的关联关系，和 Category 类似。

    author=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return  self.title

    def get_absolute_url(self):
       return  reverse('detail',kwargs={"pk":self.pk})









