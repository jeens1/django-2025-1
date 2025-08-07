from urllib import request

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from blog.models import Post
from example.serializers import PostSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework import decorators

@api_view(['GET', 'POST'])
def blogapi(request):
    if request.method == 'GET':
        posts=Post.objects.all()
        postSerializer=PostSerializer(posts,many=True)
        return Response(postSerializer.data,status=status.HTTP_200_OK)
    else:
        postserializer=PostSerializer(data=request.data)
        if postserializer.is_valid():
            postserializer.save()
            return Response(postserializer.data,
                            status=status.HTTP_201_CREATED)
    return Response(postserializer.errors,
                    status=status.HTTP_400_BAD_REQUEST)
            #화면에서 작성 json >django 서버로 전달됨
        #json >post instance로 변경 -deserialize

@api_view(['GET','DELETE','PUT'])
def postapi(request, pk):
    if request.method == 'GET':
        post = Post.objects.get(pk=pk)
        postserializer = PostSerializer(post)
        return Response(postserializer.data,status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        post=Post.objects.get(pk=pk)
        post.delete()
        return Response("delete completed",status=status.HTTP_204_NO_CONTENT)
    else:
        post=get_object_or_404(Post,pk=pk)
        post=Post.objects.get(pk=pk)
        postserializer=PostSerializer(post,data=request.data)
        if postserializer.is_valid():
            postserializer.save()
            return Response(postserializer.data,status=status.HTTP_200_OK)
    return Response(postserializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def helloapi(request):
    return Response("Hello World!")

@api_view(['GET'])
def HIapi(request):
    return Response("HI World!")

def example(request):
    return render(request,
                  'example/example.html',
    )

# Create your views here.
