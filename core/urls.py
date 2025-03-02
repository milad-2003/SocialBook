from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('settings/', views.settings, name='settings'),
    path('search/', views.search, name='search'),
    path('upload/', views.upload, name='upload'),
    path('follow-user/', views.follow_user, name='follow-user'),
    path('like-post/', views.like_post, name='like-post'),
    path('profile/<str:pk>/', views.profile, name='profile'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.logout, name='logout'),
]
