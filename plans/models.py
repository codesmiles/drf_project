from django.db import models

# Create your models here.
class Plan(models.Model):
    name = models.CharField(max_length=50)
    detail = models.TextField()
    status = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.name