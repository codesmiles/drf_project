from . import views
from django.urls import path, include


urlpatterns = [
    path('signup/', views.SIgnUpView.as_view)
]
