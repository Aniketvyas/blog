from datetime import datetime
from enum import auto
from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField

class blogs(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=1000)
    image = models.ImageField()
    content = RichTextField(blank=True,null=True)
    submitedBy = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    dateUploaded = models.DateTimeField(auto_now_add=True)
    updatedOn = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('category',on_delete=models.CASCADE)
    likes = models.IntegerField()

    def __str__(self):
        return self.title
    

class category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class comments(models.Model):
    id = models.AutoField(primary_key=True)
    post = models.ForeignKey('blogs',on_delete=models.CASCADE)
    comment = models.TextField()
    doneOn = models.DateTimeField(auto_now_add=True)
    updatedOn = models.DateTimeField(auto_now_add=True)


class tags(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class blogPlusTags(models.Model):
    id = models.AutoField(primary_key=True)
    blog = models.ForeignKey('blogs',on_delete=models.CASCADE)
    tags = models.ForeignKey('tags',on_delete=models.CASCADE)

    def __str__(self):
        return self.blog.title + " - " + self.tags.name

class newsletterSubscription(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField()
    subscribedOn = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class contactQueries(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField()
    subject = models.CharField(max_length=10000)
    phoneNumber = models.BigIntegerField()
    name = models.CharField(max_length=1000)
    message = models.TextField()

    def __str__(self):
        return self.name+ " - " + self.subject + ' - '+self.message