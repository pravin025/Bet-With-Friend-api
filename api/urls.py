from django.conf.urls import url, include
from rest_framework import routers

from api import views

router = routers.DefaultRouter()
router.register(r'groups', views.GroupViewSet)
router.register(r'events', views.EventViewSet)
router.register(r'user-profile', views.UseProfileViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'authenticate', views.CustomObtainAuthToken.as_view())
]
