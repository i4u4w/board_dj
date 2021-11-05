from django.shortcuts import redirect, render
from .models import Board, Reply
from acc.models import User
from django.utils import timezone
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    page = request.GET.get('page',1)
    cate = request.GET.get('cate','')
    kw = request.GET.get('kw','')

    if kw:
        if cate == 'sub':
            b = Board.objects.filter(subject__startswith = kw)
        elif cate == 'wri':
            b = Board.objects.filter(writer = kw)
        else:
            b = Board.objects.filter(content__contains=kw)
    else:
        b = Board.objects.all()

    b = b.order_by('-pubdate')

    pag = Paginator(b, 10)
    obj = pag.get_page(page)
    context = {
        "blist":obj,
        'cate':cate,
        'kw':kw
    }
    return render(request, 'board/index.html', context)


def remove_reply(request, rpk, bpk):
    r = Reply.objects.get(id=rpk)
    if request.user.username == r.replyer:
        r.delete()
    else:
        return render(request, "error/forbidden.html")
    return redirect("board:detail", bpk=bpk)

def create_reply(request, bpk):
    b = Board.objects.get(id=bpk)
    rep = request.user.username
    com = request.POST.get("comment")
    if com:
        Reply(sub=b, replyer=rep, comment=com).save()
    return redirect("board:detail", bpk=bpk)

def create(request):
    if request.method == "POST":
        sub = request.POST.get("subject")
        wri = request.user.username
        con = request.POST.get("content")
        Board(subject=sub, writer=wri, content=con, pubdate=timezone.now()).save()
        return redirect("board:index")
    return render(request, "board/create.html")


def detail(request, bpk):
    b = Board.objects.get(id=bpk)
    r = b.reply_set.all()
    u = User.objects.get(username=b.writer)
    context = {
        "bo":b,
        "pic":u.getpic(),
        "rep":r,
        "bwriter":u,
    }
    return render(request, "board/detail.html", context)

def delete(request, bpk):
    b = Board.objects.get(id=bpk)
    if b.writer == request.user.username:
        b.delete()
    else:
        return render(request, "error/forbidden.html")
    return redirect('board:index')


def addup(request, bpk):
    b = Board.objects.get(id=bpk)
    b.up.add(request.user)
    return redirect("board:detail", bpk=bpk)

def removeup(request, bpk):
    b = Board.objects.get(id=bpk)
    b.up.remove(request.user)
    return redirect("board:detail", bpk=bpk)