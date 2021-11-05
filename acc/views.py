from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import User


def unfollow(request, wri, bpk):
    u = User.objects.get(username=wri)
    request.user.follow.remove(u)
    return redirect('board:detail', bpk=bpk)

def follow(request, wri, bpk):
    u = User.objects.get(username=wri)
    request.user.follow.add(u)
    return redirect('board:detail', bpk=bpk)



def usermod(request):
    if request.method == "POST":
        un = request.user.username
        u = User.objects.get(username=un)
        pw = request.POST.get("password")
        ni = request.POST.get("nickname")
        co = request.POST.get("comment")
        pi = request.FILES.get("pic")
        if pw:
            u.set_password(pw)
        u.nickname = ni
        u.comment = co
        if pi:
            u.pic = pi
        u.save()
        user = authenticate(username=un, password=pw)
        login(request, user)
        return redirect('acc:profile')

    return render(request, "acc/usermod.html")

def userdel(request):
    u = User.objects.get(username=request.user.username)
    u.delete()
    return redirect("acc:index")

def profile(request):
    return render(request, "acc/profile.html")

def signup(request):
    if request.method == "POST":
        un = request.POST.get("username")
        pw = request.POST.get("password")
        nn = request.POST.get("nickname")
        co = request.POST.get("comment")
        pi = request.FILES.get("pic")
        User.objects.create_user(username=un, password=pw, nickname=nn, comment=co, pic=pi)
        return redirect("acc:index")
    return render(request, "acc/signup.html")


# Create your views here.
def index(request):
    return render(request, "acc/index.html")

def userlogin(request):
    un = request.POST.get("username")
    pw = request.POST.get("password")
    user = authenticate(username=un, password=pw)
    if user:
        login(request, user)
        messages.success(request, "LOGIN SUCCESS")
    else:
        messages.error(request, "LOGIN FAIL")
    return redirect('acc:index')

def userlogout(request):
    logout(request)
    return redirect('acc:index')


