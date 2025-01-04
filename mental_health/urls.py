from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "Mental-health Admin"
admin.site.site_title = "Mental-health Admin Portal"
admin.site.index_title = "Welcome to Mental-health"

urlpatterns = [
     
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    # path('/login',include('home.urls')),
    # path('/signup',include('home.urls')),
    # path('/homepage',include('home.urls')),
    # path('/createpost',include('home.urls')),
    # path('/profile',include('home.urls')),
]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)