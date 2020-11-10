from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    
    #author = models.CharField(max_length= 100)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=False)   #post.user  
    body = models.TextField()
    image = models.ImageField(upload_to='posts',null=True)
    created_at = models.DateTimeField()
    liked_users = models.ManyToManyField(User,related_name='liked_posts')

    def __str__(self): #게시판에 미리 보기 
        #return f'{self.author} : {self.body}'
        if self.user:
            return f'{self.user.get_username()} : {self.body}'
        
        return f'{self.body}'
