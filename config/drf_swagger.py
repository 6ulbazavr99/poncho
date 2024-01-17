# from django.urls import path
# from rest_framework import permissions
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi
#
# from drf_yasg.utils import swagger_auto_schema
# from rest_framework import serializers, status
# from rest_framework_simplejwt.views import (
#     TokenBlacklistView,
#     TokenObtainPairView,
#     TokenRefreshView,
#     TokenVerifyView,
# )
#
#
# class TokenObtainPairResponseSerializer(serializers.Serializer):
#     access = serializers.CharField()
#     refresh = serializers.CharField()
#
#     def create(self, validated_data):
#         raise NotImplementedError()
#
#     def update(self, instance, validated_data):
#         raise NotImplementedError()
#
#
# class DecoratedTokenObtainPairView(TokenObtainPairView):
#     @swagger_auto_schema(
#         responses={
#             status.HTTP_200_OK: TokenObtainPairResponseSerializer,
#         }
#     )
#     def post(self, request, *args, **kwargs):
#         return super().post(request, *args, **kwargs)
#
#
# class TokenRefreshResponseSerializer(serializers.Serializer):
#     access = serializers.CharField()
#
#     def create(self, validated_data):
#         raise NotImplementedError()
#
#     def update(self, instance, validated_data):
#         raise NotImplementedError()
#
#
# class DecoratedTokenRefreshView(TokenRefreshView):
#     @swagger_auto_schema(
#         responses={
#             status.HTTP_200_OK: TokenRefreshResponseSerializer,
#         }
#     )
#     def post(self, request, *args, **kwargs):
#         return super().post(request, *args, **kwargs)
#
#
# class TokenVerifyResponseSerializer(serializers.Serializer):
#     def create(self, validated_data):
#         raise NotImplementedError()
#
#     def update(self, instance, validated_data):
#         raise NotImplementedError()
#
#
# class DecoratedTokenVerifyView(TokenVerifyView):
#     @swagger_auto_schema(
#         responses={
#             status.HTTP_200_OK: TokenVerifyResponseSerializer,
#         }
#     )
#     def post(self, request, *args, **kwargs):
#         return super().post(request, *args, **kwargs)
#
#
# class TokenBlacklistResponseSerializer(serializers.Serializer):
#     def create(self, validated_data):
#         raise NotImplementedError()
#
#     def update(self, instance, validated_data):
#         raise NotImplementedError()
#
#
# class DecoratedTokenBlacklistView(TokenBlacklistView):
#     @swagger_auto_schema(
#         responses={
#             status.HTTP_200_OK: TokenBlacklistResponseSerializer,
#         }
#     )
#     def post(self, request, *args, **kwargs):
#         return super().post(request, *args, **kwargs)
#
# schema_view = get_schema_view(
#    openapi.Info(
#       title="Poncho API",
#       default_version='v1',
#       description="Test description",
#       terms_of_service="https://www.google.com/policies/terms/",
#       contact=openapi.Contact(email="contact@snippets.local"),
#       license=openapi.License(name="BSD License"),
#    ),
#    public=True,
#    permission_classes=(permissions.AllowAny,),
# )
#
# urlpatterns = [
#    path('docs<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
#    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
#    path('redocs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
# ]


from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Poncho API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
   path('docs<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redocs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
