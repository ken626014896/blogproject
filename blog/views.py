from django.shortcuts import render,get_object_or_404
from django.http import  HttpResponse
from blog.models import Post,Category


import  markdown

# Create your views here.
def  index(requset):
    articles=Post.objects.all().order_by('-created_time')
    for i in articles:
      print(i.get_absolute_url())
    return  render(requset,"blog/index.html",{"articles":articles


                                              })


def  detail(request,pk):
    post=get_object_or_404(Post,pk=pk)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    return render(request,"blog/detail.html",context={'post': post})



#关于归档的函数

def archives(request,year,month):
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month
                                    ).order_by('-created_time')


    return render(request, 'blog/index.html', context={'articles': post_list})



def category(request, pk):
    # 记得在开始部分导入 Category 类
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-created_time')
    return render(request, 'blog/index.html', context={'articles': post_list})


