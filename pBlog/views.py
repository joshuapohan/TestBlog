from django.shortcuts import render
from django.http import HttpResponse
from pBlog.forms import PostForm
from blogPost.models import WritePost
from django.utils import timezone

def writepost(request):
    if request.method == 'POST':
        request.POST = request.POST.copy()
        form = PostForm(request.POST)
        if form.is_valid():
            form.data['title'] = 'My huge magnum dong'
            WritePost.objects.create(date_posted=timezone.now(), blog_title=form.data['title'], blog_post=form.data['message'], post_author=form.data['user'])
            return render(request,'blog_post.html',{'form':form})
    else:
        form = PostForm(initial={'title':'enter title...','user':'enter username here...','message':'lorem ipsum....'})

    return render(request,'blog_post.html',{'form':form})

def readpost(request):
    if request.method == 'GET':
        posts = WritePost.objects.filter(date_posted__lte=timezone.now()).order_by('date_posted')
    return render(request,'blog_read.html',{'posts':posts})
