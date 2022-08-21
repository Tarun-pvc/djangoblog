from django.urls import path, include

from . import views

urlpatterns = [  # path urls are called endpoints
    path('', views.index, name='index'),
    #path('about/', views.about, name='about'),
    #path('blog/', views.blog, name='blog'),
    path('authors/', views.authors, name='authors'),
    path('authors/<id>/blogs/', views.authorblogs, name='authorblogs'),
]
