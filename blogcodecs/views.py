from django.contrib import messages
from django.shortcuts import redirect, render
from django.db.models import Subquery

from blogcodecs.models import *
import datetime as dt
import random
# Create your views here.
def home(request):
    categor = category.objects.all()
    blogsAll = blogs.objects.all()
    blogPlusTagsAll = blogPlusTags.objects.all()
    sliderBlog = blogPlusTagsAll.filter(tags=tags.objects.get(name="slider"))
    monthBlogs = blogPlusTagsAll.filter(
        tags = tags.objects.get(name="top Blogs of Month"),
        blog__in = Subquery(blogsAll.filter(dateUploaded__month=dt.datetime.now().strftime('%m')).values('id')))
    dailyBlog1 = random.choices(blogsAll)
    d2 = blogsAll.exclude(id=dailyBlog1[0].id)
    dailyBlog2 = random.choices(d2)
    trending = blogsAll.all().order_by('likes')[:10]
    print(trending)
    context = {
        'categories':categor,
        'sliderContent':sliderBlog,
        'monthContent':monthBlogs,
        'dailyBlog1': dailyBlog1[0],
        'dailyBlog2': dailyBlog2[0],
        'trendingContent':trending
    }
    return render(request,'index.html',context)

def categoryView(request,id):
    categor = category.objects.get(name=id)
    blog = blogs.objects.filter(category=categor)
    context = {
        'blogContent':blog,
        'category':categor
    }
    return render(request,'beauty.html',context)


def blogView(request,id):
    blogObject = blogs.objects.get(id=id)
    categories = category.objects.all()[:7]
    print(blogObject)
    context = {
        'blog':blogObject,
        'categories':categories
    }
    return render(request,'single.html',context)

def contact(request):
    return render(request,'contact.html')

def subscribe(request):
    if request.method == "POST":
        a= request.POST['email']
        if newsletterSubscription.objects.filter(email=a).exists():
            messages.info(request,'already subscribed')
        else:
            newsletterSubscription(
                email= a
            ).save()
            messages.info(request,'subscription sucessfull  ')
        return redirect('/')

def comment(request,id):
    if request.method == "POST":
        a = request.POST['comment']
        comments(
            post = blogs.objects.get(id=id),
            comment = a,
        ).save()
        return redirect(f'/blog/{id}')