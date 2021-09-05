
from django.db.models.fields.related import ManyToManyField
from django.shortcuts import render, redirect
from .models import Offer, Post
from django.contrib.auth.decorators import login_required
from .forms import CreatePostForm, EditPostForm, MakeOfferForm
from django.contrib import messages
from . filters import PostFilter


def home(request):

    if request.user.is_authenticated:
        cur_user = request.user
        posts = Post.objects.filter(status='აქტიური').exclude(author=cur_user)
        filter = PostFilter(request.GET, queryset=posts)
        posts = filter.qs
    else:
        posts = Post.objects.filter(status='აქტიური')
        filter = PostFilter(request.GET, queryset=posts)
        posts = filter.qs
    context = {'posts': posts, 'filter': filter}
    return render(request, 'trade_market/home.html', context)


def about(request):
    return render(request, 'trade_market/about.html')


@login_required
def my_posts(request):
    current_user = request.user
    cur_id = current_user.id
    posts = Post.objects.filter(author=current_user)
    context = {'posts': posts}
    return render(request, 'trade_market/my-posts.html', context)


@login_required
def create_post(request):
    cur_user = request.user
    post = Post()
    post.author = cur_user
    if request.method == 'POST':
        form = CreatePostForm(request.POST, instance=post)
        if form.is_valid:
            form.save()
            return redirect('my_posts')
    else:
        form = CreatePostForm(instance=post)
    context = {'form': form}
    return render(request, 'trade_market/create-post.html', context)


@login_required
def make_offer(request, pk):
    cur_post = Post.objects.get(id=pk)
    author = cur_post.author
    if request.user != author:
        form = MakeOfferForm()
        if request.method == 'POST':
            form = MakeOfferForm(request.POST)
            if form.is_valid:
                form.instance.post = cur_post
                form.instance.author = request.user
                form.save()
                return redirect('home')
        context = {'form': form}
        return render(request, 'trade_market/make-offer.html', context)
    else:
        return render(request, 'trade_market/no-access.html')


@login_required
def view_offer(request, pk):
    cur_post = Post.objects.get(id=pk)
    allowed_user = cur_post.author
    if allowed_user == request.user:
        offers = Offer.objects.filter(post=cur_post)
        context = {'offers': offers}
        return render(request, 'trade_market/offers.html', context)
    else:
        return render(request, 'trade_market/no-access.html')


@login_required
def edit_post(request, pk):
    cur_post = Post.objects.get(id=pk)
    allowed_user = cur_post.author
    if allowed_user == request.user:
        form = EditPostForm(instance=cur_post)
        if request.method == 'POST':
            form = EditPostForm(request.POST, instance=cur_post)
            if form.is_valid:
                form.save()
                return redirect('my_posts')
        context = {'form': form, 'id': pk}
        return render(request, 'trade_market/edit-post.html', context)
    else:
        return render(request, 'trade_market/no-access.html')


@login_required
def delete_post(request, pk):
    cur_post = Post.objects.get(id=pk)
    allowed_user = cur_post.author
    if allowed_user == request.user:
        cur_post.delete()
        return render(request, 'trade_market/deleted.html')
    else:
        return render(request, 'trade_market/no-access.html')
