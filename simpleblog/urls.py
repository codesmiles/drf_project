from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls')),
    path('', include('plans.urls')),
    path('comments/', include('comments.urls')),
    path('auth/', include('accounts.urls')),
    path('payment/', include('payment.urls')),
]
