from django.db import models

# Create your models here.
class My_video(models.Model):
    title=models.CharField(max_length=200)
    video_thumbnail= models.ImageField(default='black_image.jpg')
    videofile= models.FileField(upload_to='video/%y',default='')
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (self.title)



class Comment(models.Model):
    comment=models.TextField()
    commented_by= models.TextField() 
    title= models.ForeignKey(My_video, related_name='comments' , on_delete=models.CASCADE)
    date= models.DateTimeField(auto_now_add=True)
