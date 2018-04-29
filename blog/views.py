from django.shortcuts import render,get_object_or_404
from django.http import  HttpResponse
from blog.models import Post,Category

from comments.forms import CommentForm
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
    # 记得在顶部导入 CommentForm
    form = CommentForm()
    # 获取这篇 post 下的全部评论
    comment_list = post.comment_set.all()

    # 将文章、表单、以及文章下的评论列表作为模板变量传给 detail.html 模板，以便渲染相应数据。
    context = {'post': post,
               'form': form,
               'comment_list': comment_list
               }
    return render(request,"blog/detail.html",context=context)




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


