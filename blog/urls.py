from django.urls import path
from . import views
from .views import category

urlpatterns=[
    #    127.0.0.1:8000/blog/
    #/blog/catalog/slug
    path('category/<slug>/',views.category,name='category'),
    path('', views.index ),
    path('<int:pk>/', views.detail ),
    path('create/', views.create ,name='blogcreate'),
    path('createfake/',views.createfake),

]