from django.urls import path
from . import views

app_name= 'my_videos'

urlpatterns = [
    path('', views.goto_videos, name='videos'),
    path('<slug:slug>', views.goto_video, name='video'),
    path('send-comment/', views.send_comment, name='send_comment'),
]
