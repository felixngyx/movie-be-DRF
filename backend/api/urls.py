from rest_framework.routers import DefaultRouter
from .views import HomeViewSet, AuthViewSet, MovieViewSet, ChannelViewSet

router = DefaultRouter()
router.register(r'home', HomeViewSet, basename='home')
router.register(r'auth', AuthViewSet, basename='auth')
router.register(r'movies', MovieViewSet, basename='movie')
router.register(r'channels', ChannelViewSet, basename='channel')

urlpatterns = router.urls