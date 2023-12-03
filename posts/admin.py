from django.contrib import admin
from .models import Post,Comment,Category

class PostAdmin(admin.ModelAdmin):
    list_display=['title','draft','auhtor']
    list_filter=['publish_date']
    search_fields=['title']

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)


