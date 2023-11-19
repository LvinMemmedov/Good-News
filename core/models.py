from django.db import models

# Create your models here.
class BaseModel(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        abstract=True
    



class News (BaseModel):
    title=models.CharField(max_length=255)
    content=models.TextField()
    imge=models.ImageField(upload_to='news',null=True,blank=True)
    
