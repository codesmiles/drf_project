from django.db import models

# Create your models here.

"""
Class Posts
    id:int
    title:string(50)
    content:text
    created_at:datetime
"""
    
class Post(models.Model):
    title= models.CharField(max_length=50)
    content= models.TextField()
    slug = models.CharField(max_length=20, null=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.title