from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ),
    path('user_oto/', include('auth_user_oto.urls')),
    path('abstract_user/', include('auth_abstract_user.urls')),
    path('abstract_base_user', include('auth_abstract_base_user.urls')),
]
