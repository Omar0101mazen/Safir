from django.db import models
from django.utils.text import slugify
# Create your models here.



class Linke(models.Model):
    link = models.URLField(blank=True,null=True)  
    expiration_date = models.DateTimeField(db_index=True)
    employee_name = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50,blank=True,null=True)
    
    count_of_clients = models.IntegerField(default=0)
    number_of_url = models.SlugField(null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    now = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.link  

    
    def save(self,*args, **kwargs):
        self.number_of_url = slugify(self.pk)
        super(Linke,self).save(*args, **kwargs)

class Add_video(models.Model):
    video = models.URLField(blank=True,null=True)
    
    def __str__(self):
        return self.video  