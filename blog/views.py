from django.shortcuts import render, redirect

from .forms import PostForm
from .models import Post, Category,slug
# Create your views here.
from django.shortcuts import render,redirect

#함수 생성
def index(request):
    #db에서 query - select * from post
    posts1111 = Post.objects.all().order_by('-pk')
    categories=Category.objects.all()
    return render(request,
                  'blog/index.html',
                  context={'posts':posts1111,'categories':categories}
                )
def category(request,slug):
    categories=Category.objects.all()
    category=Category.objects.get(slug=slug)
    posts=Post.objects.filter(category=category)
    return render(request,
                  template_name='blog/index.html',
                  context={'posts':posts,'categories':categories})



def detail(request, pk):
    categories = Category.object.all()
    if slug=='no_category':
        posts_category = Post.objects.all()
       # 미분류인경우
    else:
        category= Category.objects.get(slug=slug)
        posts=Post.objects.filter(category=category)


        return render(request,
                  'blog/detail.html',
                  context={'posts':posts,
                           'categories':categories})
#/blog에 크리에이트가  호출되면

def create(request):
    if request.method=="POST":
        postform = PostForm(request.POST,request.FILES)
        #포스트 폼을 쓰긴할건데 리퀘스트 안에 있는걸로 하겠다
        if postform.is_valid():
            #사용자가 만든게 아니라 장코에서 만들어준다1
            post1=postform.save(commit=False)
            #포스트 폼에 세이브를 해라
            post1.title=post1.title+"홍길동 만세"
            #가지고 왔지만 추가적으로 글을 넣고 싶을때

            #post1.author = request.user           \
            post1.save()
            #위에 글들을 저장
            return redirect('/blog/')
            #정상값인 경우
#비정상인경우
    #작성하다가 제출버튼을 누른경우
    else:#get #get 세글작성하기 버튼을 눌러서 create()함수로 들어온 경우
        postform = PostForm()
        #타이틀 이미지 다들어있지만 비어있다

    return render(request,
                  template_name='blog/postform.html'
                  ,context={'postform':postform})
def createfake(request):
    post=Post()
    post.title="새싹 용산구"
    post.content="나진상가 3층"
    post.save()
    return redirect('index')
