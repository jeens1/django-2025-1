
from django.urls import path

import example
from . import views
urlpatterns = [
    path('',views.example, name='example'),
    path('helloapi/',views.helloapi, name='helloapi'),
    path('HIapi/',views.HIapi, name='HIapi'),
    path('postapi/<int:pk>/',views.postapi, name='postapi'),
    path('blogapi/',views.blogapi, name='blogapi'),
]