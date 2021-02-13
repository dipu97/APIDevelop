from django.urls import include, path
from rest_framework.routers import DefaultRouter

from APIapp.views import IndexViewSet

router = DefaultRouter()
router.register('', IndexViewSet)

# # The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
 ]