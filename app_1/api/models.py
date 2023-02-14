from django.db import models

from django.contrib.auth.models import User
class likes(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    likes_total_count=models.IntegerField()

class blog(likes):
    sam=models.OneToOneField(likes,on_delete=models.CASCADE,parent_link=True)
    # user=models.ForeignKey(User,on_delete=models.CASCADE)
    caption=models.CharField(max_length=50)
    article=models.TextField(max_length=100)
    
    # likes_count=models.IntegerField()
 
# class use(models.Model):
#     username=models.ForeignKey(User,on_delete=models.CASCADE)
#     first_name=models.CharField(max_length=50)
#     last_name=models.CharField(max_length=40)
#     emial=models.CharField(max_length=10)