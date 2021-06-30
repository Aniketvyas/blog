
# from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home),
    path('category/<str:id>',views.categoryView),
    path('blog/<str:id>',views.blogView),
    path('contact',views.contact),
    path('subscribe',views.subscribe),
    path('comment/<str:id>',views.comment),
    path('submitForm',views.contactQuery),
    path('dashboard',views.dashboardView),
    path('addBlog',views.addBlog),
    path('update/<str:id>',views.updateBlog),
    path('delete/<str:id>',views.deleteBlog)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)