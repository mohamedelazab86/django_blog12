"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from posts.views import list_post,detail_post,create_post,update_post,delete_post
from posts.api import list_api,detail_api,List_Api,Detail_APi
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

...

schema_view = get_schema_view(
   openapi.Info(
      title="blog API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

from posts.views2 import List_post,Detail_post,Create_post,Update_post,Delete_post
urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/',list_post),
    path('create/',create_post),
    path('details/<int:pk>',detail_post),
    path('update/<int:pk>',update_post),
    path('delete/<int:pk>',delete_post),

    path('list_api/',list_api),
    path('details/api/<int:pk>',detail_api),

    path('List_api',List_Api.as_view()),
    path('Detail_api/<int:pk>',Detail_APi.as_view()),
     path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

   path('posts/',List_post.as_view()),
   path('Create11/',Create_post.as_view()),
   path('Details11/<int:pk>',Detail_post.as_view()),
   path('Update11/<int:pk>',Update_post.as_view()),
   path('Delete11/<int:pk>',Delete_post.as_view()),
   


]
urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
