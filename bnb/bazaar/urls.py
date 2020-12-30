from django.urls import path
from . import views
urlpatterns = [

    path('', views.index),
    path('loginsignup/', views.loginsignup),
    path('signup/', views.signup),
    path('loginuser/', views.loginuser),
    path('logoutuser/', views.logoutuser),
    path('profile/', views.profile),
    path('letsprofile/', views.letsprofile),
    path('buy/', views.buy),
    path('sell/', views.sell),
    path('letssell/', views.letssell),
    path('news/', views.news),
    path('winner/', views.winner),
    path('letsbuy/', views.letsbuy),
    path('letsbuymb/', views.letsbuymb),
    path('letsupdatetime/', views.letsupdatetime),
    path('letsupdatetext/', views.letsupdatetext),
]
