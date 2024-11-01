from rest_framework.routers import DefaultRouter
from .views import HomeViewSet, AuthViewSet

router = DefaultRouter()
router.register(r'home', HomeViewSet, basename='home')
router.register(r'auth', AuthViewSet, basename='auth')

urlpatterns = router.urls