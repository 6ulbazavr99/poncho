from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Poncho API",
      default_version='v1',   # TODO:
      description="""
///////////////////////////////////////////////////////////////////////////////////////////////////
account:
customuser: permissions, model, serializers, views, admin, urls +
customuser: phone, celery ?
vendor: start +


product:
category: model, serializers, views, admin, urls +
category: slug, mptt ?


config:
settings: fix jwt +


///////////////////////////////////////////////////////////////////////////////////////////////////

Reg. temple:

{
  "username": "andrey",
  "email": "andrey@andrey.com",
  "password": "bastard123",
  "password2": "bastard123",
  "first_name": "andrey",
  "last_name": "test",
  "birthdate": "2000-01-23"
}
      """,
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
