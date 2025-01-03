from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="home"),
    path('login',views.login,name="login"),
    path('signup',views.signup,name="signup"),
    path('homepage',views.homepage,name="homepage"),
    path('createpost',views.createpost,name="createpost"),
    path('profile',views.profile,name="profile"),
]