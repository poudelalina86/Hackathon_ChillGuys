from django.contrib import admin
from django.urls import path, include
from home import views
from users import views as user_views
from .views import PostListView , PostDetailView, PostCreateView, PostUpdateView, PostDeleteView


urlpatterns = [
  path('admin/', admin.site.urls),
    path('',views.index,name="home"),
    path('signup',user_views.signin, name='signin'),
    path('signinauth',user_views.signin_auth,name='signinauth'),
    path('loginpage',user_views.login_page,name="loginpage"),
    path('')
    path('homepage', PostListView.as_view(),name='homepage'),
    path('homepage/post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('homepage/post/create/', PostCreateView.as_view(),name='post-create'),
    path('homepage/post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('homepage/post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    # path('postComment', views.postComment, name="postComment"),
    path('profile',user_views.profile,name="profile"),
    path('logout',views.logoutuser,name="logout"),
]

