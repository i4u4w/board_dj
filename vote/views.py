from django.shortcuts import redirect, render
from .models import Topic, Choice
from acc.models import User
from django.utils import timezone
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    page = request.GET.get("page", 1)
    
    t = Topic.objects.all().order_by("-ctime")
    pag = Paginator(t, 4)
    obj = pag.get_page(page)
    
    context = {
        "topics": obj,
    }
    return render(request,"vote/index.html", context)

def create(request):
    if request.method == "POST":
        top = request.POST.get("topic")
        wri = request.user.username
        con = request.POST.get("content")
        t = Topic(subject=top, writer=wri, ctime=timezone.now(), content=con)
        t.save()
        sels = request.POST.getlist("select")
        coms = request.POST.getlist("comment")
        pics = request.FILES.getlist("pic")
        for i,j,k in zip(sels, coms, pics):
            Choice(sub=t, select=i, comment=j, pic=k).save()
        return redirect("vote:index")

    return render(request, "vote/create.html")


def cancel(request, tpk):
    t = Topic.objects.get(id=tpk)
    t.voter.remove(request.user)
    c = t.choice_set.all()
    for i in c:
        if request.user in i.voter.all():
            i.voter.remove(request.user)
    return redirect("vote:detail", tpk=tpk)
    


def vote(request,tpk):
    t = Topic.objects.get(id=tpk)
    if not request.user in t.voter.all():
        t.voter.add(request.user)
        s = request.POST.get("select")
        c = Choice.objects.get(id=s)
        c.voter.add(request.user)
    return redirect('vote:detail', tpk=tpk)


def detail(request, tpk):
    print(dir(request.user))
    t = Topic.objects.get(id=tpk)
    u = User.objects.get(username=t.writer)
    c = t.choice_set.all()
    context = {
        "topic" : t,
        "choices" : c,
        "pic":u.getpic()
    }
    return render(request, "vote/detail.html", context)
