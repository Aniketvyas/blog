# from blog.blog.settings import EMAIL_HOST_USER
from django.contrib import messages
from django.shortcuts import redirect, render
from django.db.models import Subquery
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.core.paginator import Paginator
from blogcodecs.models import *
import datetime as dt
import random
# Create your views here.
def home(request):
    # print(request)
    categor = category.objects.all()[:3]
    blogsAll = blogs.objects.all()
    blogPlusTagsAll = blogPlusTags.objects.all()
    sliderBlog = blogPlusTagsAll.filter(tags=tags.objects.get(name="slider"))
    monthBlogs = blogPlusTagsAll.filter(
        tags = tags.objects.get(name="top Blogs of Month"),
        # blog__in = Subquery(blogsAll.filter(dateUploaded__month=dt.datetime.now().strftime('%m')).values('id'))
        )
    dailyBlog1 = random.choices(blogsAll)
    d2 = blogsAll.exclude(id=dailyBlog1[0].id)
    dailyBlog2 = random.choices(d2)
    trending = blogsAll.all().order_by('likes')[:10]
    print(monthBlogs)
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
    paginator = Paginator(blog,9)
    page = request.GET.get('page')
    galler = paginator.get_page(page)
    context = {
        'gallery':galler,
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

def contactQuery(request):
    if request.method == "POST":
        print(request.POST)
        name  = request.POST['name']
        subject = request.POST['subject']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        if contactQueries.objects.filter(name=name,subject=subject,email=email,phoneNumber=phone,message=message).exists():
            # email = EmailMessage(subject, 
            #         message, settings.EMAIL_HOST_USER, ['vyasaniket6@gmail.com'])
            # email.fail_silently = False
            # email.send()
            messages.info(request,'Your Query is Already Submited!')
            return redirect('/contact')
        else:
            contactQueries(
                name=name,
                email=email,
                subject = "Website Query: " + subject,
                message=message,
                phoneNumber = phone
            ).save()
            email = EmailMessage("Website Query: "+ subject, 
                    message, settings.EMAIL_HOST_USER, ['vyasaniket6@gmail.com'])
            email.fail_silently = False
            email.send()
            messages.info(request,'Request Submited Successfully!')
            return redirect('/')


def dashboardView(request):
    dataObject = blogs.objects.filter(submitedBy=request.user).order_by('-dateUploaded')
    paginator = Paginator(dataObject,9)
    page = request.GET.get('page')
    galler = paginator.get_page(page)
    context = {
        # 'gallery':galler,
        'categoryPacket':category.objects.all(),
        'gallery':galler,
    }
    return render(request,'dashboard.html',context)

def addBlog(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        image = request.FILES['image']
        categor = category.objects.get(id=request.POST['category'])
        blogs(
            title=title,
            image=image,
            submitedBy=request.user,
            category=categor,
            likes=0
        ).save()
        messages.info(request,'Uploaded Successfully!')
        return redirect('/dashboard')

def updateBlog(request,id):
    if request.method == "POST":
        print(request.POST)
        title = request.POST['title']
        content = request.POST['content']
        image = request.FILES['image']
        categor = category.objects.get(id=request.POST['category'])
        blogs.objects.filter(id=id).update(title=title,content=content,image=image,category= categor)
        messages.info(request,'Updated Successfully!')
        return redirect('/dashboard')

def deleteBlog(request,id):
    blogs.objects.get(id=id).delete()
    messages.info(request,'deleted Succesfully!')
    return redirect('/dashboard')