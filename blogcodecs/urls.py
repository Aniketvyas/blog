
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
    path('comment/<str:id>',views.comment)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)