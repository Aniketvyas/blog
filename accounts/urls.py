from django.urls import path
from django.urls.resolvers import URLPattern 
from . import views

urlpatterns = [
    path('login',views.login),
    path('logout/',views.logout)
]