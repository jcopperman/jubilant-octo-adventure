
from django.urls import path
from django.urls import include

from . import views

urlpatterns = [
    path('', views.allblogs, name='allblogs'),
    path('<int:blog_id>/', views.detail, name='detail'), 
    path('summernote/', include('django_summernote.urls')),

]
