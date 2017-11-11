from django.conf.urls import url, include

from .views import MemberViewSet
from rest_framework import routers


router = routers.DefaultRouter()

# CRUD routes for Members
router.register(r'members', MemberViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
