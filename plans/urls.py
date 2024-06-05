from django.urls import path,include
from . import views
from .views import PlanViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('plans', PlanViewset, basename='plans') # registering the viewsets
urlpatterns = [
    path("", include(router.urls))
]

#routers allow you to map viewset unto our url and viewset generates to our actions 
