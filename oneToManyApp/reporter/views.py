from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.shortcuts import get_object_or_404

def index(request):
    context = {}
    context['article'] = Article.objects.all()
    return render(request, "index.html", context)

def reporterform(request):
    return render(request, "addreporter.html")

def addreporter(request):
    try:
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        r = Reporter(first_name=fname, last_name=lname, email=email)
        r.save()
        return HttpResponse("<script>alert('success'); window.location.href='./';</script>")
    except ValueError:
        return HttpResponse("<script>alert('try again'); window.location.href='./';</script>")

def articleform(request):
    context = {}
    context['reporter'] = Reporter.objects.all()
    return render(request, "addarticle.html", context)

def addarticle(request):
    rid = request.POST['reporter']
    reporter = get_object_or_404(Reporter, id=rid)
    headline = request.POST['headline']
    pbdate = request.POST['pbdate']
    a = Article(headline=headline, pub_date=pbdate, reporter=reporter)
    a.save()
    return HttpResponse("<script>alert('success'); window.location.href='./';</script>")

def viewreporter(request):
    context = {}
    context['reporter'] = Reporter.objects.all()
    return render(request, "viewreporter.html", context)

def viewarticle(request, id=None):
    context = {}
    context['article'] = Article.objects.filter(reporter=id)
    return render(request, "viewarticle.html", context)