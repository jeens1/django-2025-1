from django.urls import path
from . import views
from .views import category, PostListView, PostCreateView
from .views import PostListView
urlpatterns=[
    #    127.0.0.1:8000/blog/
    #/blog/catalog/slug
    path('',PostListView.as_view(),name='index'),
    path('category/<slug>/',views.category,name='category'),
    path('blog/create/',PostCreateView.as_view(),name='create'),
    #path('', views.index , name='index'),
    #path('<int:pk>/', views.detail ),

   # path('create/', views.create ,name='blogcreate'),

  #  path('<int:pk>/delete/',views.delete,name='blogdelete'),
   # path('<int:pk>/update/',views.update,name='blogupdate'),
    path('tag/<slug>/', views.tag, name='tag'),


    path('<int:pk>/deletecomment', views.deletecomment, name='deletecomment'),
    path('<int:pk>/updatecomment', views.updatecomment, name='updatecomment'),
    path('<int:pk>/createcomment/', views.createcomment, name='createcomment'),
    path('createfake/',views.createfake),
]
