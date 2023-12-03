from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
import datetime
from django.utils.text import slugify

# Create your models here.
# create data base    ------ model   ormm  هو عبارة عن حارس على قاعدة البيانات والمسئول عن التعامل مع قاعدة البيانات وتحويل كودبايثون العادى الى كود sql
class Post(models.Model):

    title=models.CharField(max_length=100,verbose_name=_('name_post'))
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='post_author')
    content=models.TextField(max_length=1000)
    draft=models.BooleanField(default=True)
    publish_date=models.DateTimeField(auto_now=True)
    image=models.ImageField(upload_to='photo/%y-%m-%d')
    tags = TaggableManager()
    category=models.ForeignKey('Category',on_delete=models.CASCADE,related_name='post_category')
    slug=models.SlugField(null=True,blank=True)





    def __str__(self):
        return self.title
    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.title)
        super(Post,self).save(*args,**kwargs)
class Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comment_post')
    content=models.TextField(max_length=500)
    publish_date=models.DateTimeField(default=datetime.datetime.now)
    author=models.CharField(max_length=100)

    def __str__(self):
        return str(self.post)

    

    


