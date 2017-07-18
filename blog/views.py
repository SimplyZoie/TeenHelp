from django.shortcuts import render
from django.utils import timezone
from .models import Post, Comment
from django.shortcuts import render, get_object_or_404
from .forms import PostForm, CommentForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('blog/homepage.html')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def homepage(request):
    return render(request, 'blog/homepage.html')

def post_list_self_esteem(request):
    posts = Post.objects.filter(published_date__lte=timezone.now(), category__contains='self-esteem').order_by('published_date')
    return render(request, 'blog/post_list_self-esteem.html', {'posts': posts})
    Post.objects.get(pk=pk)

def post_list_body_image(request):
    posts = Post.objects.filter(published_date__lte=timezone.now(), category__contains='body-image').order_by('published_date')
    return render(request, 'blog/post_list_body-image.html', {'posts': posts})
    Post.objects.get(pk=pk)

def post_list_stress(request):
    posts = Post.objects.filter(published_date__lte=timezone.now(), category__contains='stress').order_by('published_date')
    return render(request, 'blog/post_list_stress.html', {'posts': posts})
    Post.objects.get(pk=pk)

def post_list_bullying(request):
    posts = Post.objects.filter(published_date__lte=timezone.now(), category__contains='bullying').order_by('published_date')
    return render(request, 'blog/post_list_bullying.html', {'posts': posts})
    Post.objects.get(pk=pk)

def post_list_depression(request):
    posts = Post.objects.filter(published_date__lte=timezone.now(), category__contains='depression').order_by('published_date')
    return render(request, 'blog/post_list_depression.html', {'posts': posts})
    Post.objects.get(pk=pk)

def post_list_cyber_addiction(request):
    posts = Post.objects.filter(published_date__lte=timezone.now(), category__contains='cyber-addiction').order_by('published_date')
    return render(request, 'blog/post_list_cyber-addiction.html', {'posts': posts})
    Post.objects.get(pk=pk)


def post_list_drinking_smoking(request):
    posts = Post.objects.filter(published_date__lte=timezone.now(), category__contains='drinking-smoking').order_by('published_date')
    return render(request, 'blog/post_list_drinking-smoking.html', {'posts': posts})

def post_list_teen_pregnancy(request):
    posts = Post.objects.filter(published_date__lte=timezone.now(), category__contains='teen-pregnancy').order_by('published_date')
    return render(request, 'blog/post_list_teen-pregnancy.html', {'posts': posts})
    Post.objects.get(pk=pk)

def post_list_underage_sex(request):
    posts = Post.objects.filter(published_date__lte=timezone.now(), category__contains='underage-sex').order_by('published_date')
    return render(request, 'blog/post_list_underage-sex.html', {'posts': posts})
    Post.objects.get(pk=pk)

def post_list_child_abuse(request):
    posts = Post.objects.filter(published_date__lte=timezone.now(), category__contains='child-abuse').order_by('published_date')
    return render(request, 'blog/post_list_child-abuse.html', {'posts': posts})
    Post.objects.get(pk=pk)

def post_list_peer_pressure(request):
    posts = Post.objects.filter(published_date__lte=timezone.now(), category__contains='peer-pressure').order_by('published_date')
    return render(request, 'blog/post_list_peer-pressure.html', {'posts': posts})
    Post.objects.get(pk=pk)

def post_list_eating_disorders(request):
    posts = Post.objects.filter(published_date__lte=timezone.now(), category__contains='eating-disorders').order_by('published_date')
    return render(request, 'blog/post_list_eating-disorders.html', {'posts': posts})
    Post.objects.get(pk=pk)

def post_list_LGBTQ(request):
    posts = Post.objects.filter(published_date__lte=timezone.now(), category__contains='LGBTQ').order_by('published_date')
    return render(request, 'blog/post_list_LGBTQ.html', {'posts': posts})
    Post.objects.get(pk=pk)

def post_list_strict_parents(request):
    posts = Post.objects.filter(published_date__lte=timezone.now(), category__contains='strict-parents').order_by('published_date')
    return render(request, 'blog/post_list_strict-parents.html', {'posts': posts})
    Post.objects.get(pk=pk)

def post_list_sleep(request):
    posts = Post.objects.filter(published_date__lte=timezone.now(), category__contains='sleep').order_by('published_date')
    return render(request, 'blog/post_list_sleep.html', {'posts': posts})
    Post.objects.get(pk=pk)



def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)
