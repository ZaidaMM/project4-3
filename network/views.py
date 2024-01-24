import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import JsonResponse
from django.shortcuts import HttpResponse, HttpResponseRedirect, render, get_object_or_404
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator

from .models import User, Post, Like, Follower

def add_unlike(request, post_id):
    post = Post.objects.get(pk=post_id)
    user = User.objects.get(pk=request.user.id)
    like = Like.objects.filter(user=user, post=post)
    like.delete()

    if post.like <= 0:
        return
    else:
        post.like -= 1
        post.save()

    return JsonResponse({"message": "Post unliked successfully",})

def add_like(request, post_id):
    post = Post.objects.get(pk=post_id)
    user = User.objects.get(pk=request.user.id)
    newLike = Like(user=user, post=post)
    newLike.save()

    post.like += 1
    post.save()

    # return HttpResponseRedirect(reverse("index"))

    return JsonResponse({"message": "Post liked successfully",})

def edit(request, post_id):
    if request.method == "POST":
        data = json.loads(request.body)
        edit_post = Post.objects.get(pk=post_id)
        edit_post.content = data["content"]
        edit_post.save()

        # return HttpResponseRedirect(reverse("index"))
    
        return JsonResponse({"message": "Post edited successfully", "data":data["content"]})
   

def index(request):
    posts = Post.objects.all().order_by('id').reverse()

    # Pagination, show 10 psots per page
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    allLikes = Like.objects.all()

    postsLiked = []

    try:
        for like in allLikes:
            if like.user.id == request.user.id:
                postsLiked.append(like.post.id)
    except:
        postsLiked = []

    return render(request, "network/index.html", {
        'posts': posts,
        'page_obj': page_obj,
        'postsLiked': postsLiked
    })

   



def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")

# @csrf_exempt
def compose(request):
    # Creating a new post must be via POST
    if request.method == "POST":
        body = request.POST["compose-body"]
        user = User.objects.get(pk=request.user.id)
        post = Post(content = body, user = user)
        post.save()

        return HttpResponseRedirect(reverse("index"))
   
    else:
        return JsonResponse({"error": "POST request required"}, status=400)
    
def profile(request, user_id):
    user = get_object_or_404(User, id=user_id)

    # Filter posts by user
    posts = Post.objects.filter(user = user).order_by('id').reverse()

    # Pagination, show 10 posts per page
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "network/profile.html", {
        'posts': posts,
        'page_obj': page_obj,
        'username': user.username,
        'profile_owner': user,
      
    
    })

def following(request):
    # Get the users the current user is following
    following_users = Follower.objects.filter(follower=request.user).values_list('followed', flat=True)

    # Get posts from the users the current user is following
    following_posts = Post.objects.filter(user__in=following_users).order_by('-timestamp')

    context = {
        'following_posts': following_posts,
    }

    return render(request, 'network/following.html', context)

def follow_unfollow(request, user_id):
    target_user = User.objects.get(pk=user_id)

    if request.user in target_user.followers.all():
        request.user.following.remove(target_user)
        following_count = request.user.following.count()
        is_following = False
    else:
        request.user.following.add(target_user)
        following_count = request.user.following.count()
        is_following = True

    return JsonResponse({
        'message': 'Follow/Unfollow successful',
        'following_count': following_count,
        'is_following': is_following
    })
                




    
