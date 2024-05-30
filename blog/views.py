from django.contrib.auth import login,logout
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
# Create your views here.
from .models import Post,Category,UserProfile,Comment
from .forms import PostForm,Category_form,LoginForm,RegisterForm,CommentForm
from django.contrib.auth.decorators import permission_required


def all_posts(request):
    posts = Post.objects.all()

    context = {
        'posts': posts,

        'title': "Barcha mahsulotlar"
    }
    return render(request,'blog/index.html',context=context)


def posts_by_category(request,category_id):
    posts = Post.objects.filter(category_id=category_id)

    category = Category.objects.get(pk=category_id)
    context = {
        'posts': posts,

        'title':f"{category.title} ga tegishli mahsulotlar"
    }
    return render(request,'blog/index.html',context=context)


def post_detail(request,pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)
    form = CommentForm()
    post.views +=1
    post.save()
    context = {
        'post':post,
        'title':post.name,
        'form':form,
        'comments':comments
    }
    return render(request,'blog/detail.html',context=context)


@permission_required('blog.add_post',login_url='index')
def post_created(request):
    form = PostForm(data=request.POST,files=request.FILES)
    if form.is_valid():
        messages.success(request,"Mahsulot muvaffaqiyatli saqlandi")
        post = form.save(commit=False)
        post.author = request.user
        form.save()
    form = PostForm()
    context = {
        'form': form
    }
    return render(request,'blog/post_form.html',context)
@permission_required('blog.add_category',login_url='index')
def category_created(request):
    form = Category_form(data=request.POST)
    if form.is_valid():
        form.save()
    context = {
        'form':form
    }
    return render(request,'blog/category_form.html',context)

@permission_required('blog.change_post',raise_exception=True)
def post_ubdare(request,pk):
    post = Post.objects.get(pk=pk)
    form = PostForm(data=request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        messages.success(request,"Mahsulot muvaffaqiyatli o'zgartirildi")
        return redirect('post_detail',pk=pk)
    context = {
        'form':form
    }
    return render(request,'blog/post_form.html',context)
@permission_required('blog.change_category',raise_exception=True)
def category_ubdate(request,pk):
    category = Category.objects.get(pk=pk)
    form = Category_form(data=request.POST or None,instance=category)
    if form.is_valid():
        form.save()
        return redirect('post_detail',pk=pk)
    context = {
        'form': form
    }
    return render(request,'blog/category_form.html',context)

@permission_required('blog.delete_post',raise_exception=True)
def post_delete(request,pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        post.delete()
        messages.success(request,"Mahsulot muvaffaqiyatli o'chirildi")
        return redirect('index')


    context = {
        'post':post
    }
    return render(request,'blog/post_delete.html',context)


@permission_required('blog.delete_category',raise_exception=True)
def category_delete(request,pk):
    category = Category.objects.get(pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('index')
    context = {
        'category':category
    }
    return render(request,'blog/category_delete.html',context)



def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            messages.success(request,f"Saytga hush kelibsiz! {user.username}")
            return redirect('index')
        if form.errors:
            for error in form.error_messages.values():
                messages.error(request,str(error))


    form = LoginForm()
    context = {
        'form':form
    }
    return render(request,'blog/user_login.html',context)

def user_logout(request):
    logout(request)
    messages.warning(request,"Siz saytdan chiqdingiz")
    return redirect('login')


def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,f"siz muaffaqiyatli royhatdan o'tdingiz!")
            return redirect('login')

        if form.errors:
            for error in form.error_messages.values():
                messages.error(request,str(error))
    form = RegisterForm()
    context = {
        'form':form,
        'title':"Registratsiya"
    }
    return render(request,'blog/register.html',context)


def profile(request,username):
    if request.user.is_authenticated and request.user.username == username:
        user = User.objects.get(username=username)
        posts = Post.objects.filter(author=user)
        context = {
            'user':user,
            'title': f"{user.username} profili",
            'posts': posts
        }
        try:
            user_profile = UserProfile.objects.get(user=user)
            context['user_profile'] = user_profile
        except:
            pass
        return render(request,'blog/profile.html',context)
    else:
        return HttpResponse("Page not Found")


def create_comment(request,post_id):
    post = Post.objects.get(pk=post_id)
    if request.method == 'POST':

        form = Category_form(data=request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            messages.success(request,'komentarya saqlandi!')
    return redirect("post_detail",pk=post_id)

