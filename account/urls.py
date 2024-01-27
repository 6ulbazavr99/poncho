from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from account.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'', UserViewSet)


urlpatterns = [
    path('authorization/login/', TokenObtainPairView.as_view()),
    path('authorization/refresh/', TokenRefreshView.as_view()),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),

]


urlpatterns += router.urls
