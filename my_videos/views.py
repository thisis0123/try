from django.shortcuts import render, redirect
from .models import My_video, Comment
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='users:signin')
def goto_videos(request):
    videos= My_video.objects.all().order_by('-date')
    return render(request,'my_videos/videos.html', {'videos':videos})

@login_required(login_url='users:signin')
def goto_video(request,slug):
    video= My_video.objects.get(id=slug)
    all_videos= My_video.objects.all().order_by('-date')


    return render(request,'my_videos/video.html',{'video':video,'all_videos':all_videos})


def send_comment(request):
    username=request.POST['username']
    comment=request.POST['comment']
    id=request.POST['id']

    obj = Comment.objects.create(commented_by=username,comment=comment,title=My_video.objects.get(id=id))

    return redirect('my_videos:video', slug=id)
