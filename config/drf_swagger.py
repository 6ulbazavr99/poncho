from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Poncho API",
      default_version='v1',   # TODO:
      description="""

admin:
Token eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoyMzEwMzYzMzgyLCJpYXQiOjE3MDYxNjgxODIsImp0aSI6IjI3ZTVkYzQ5Y2NlZDRlZjFiMTVkYjJlY2NlNWE5MjIxIiwidXNlcl9pZCI6MX0.kNm7rh_n9TE_00hwUksicem-nVvX0XgUVdCi2jXiWxQ

andrey:
Token eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoyMzEwMzYzMTAwLCJpYXQiOjE3MDYxNjc5MDAsImp0aSI6ImI3ZDQzZGFlNjhmZjQ0ZjFiZmJhYjYyZWNhZGNjZDBiIiwidXNlcl9pZCI6Mn0.GLy4e1iiEHTRmG0boyn2sCX0NKX4Ta-f6JU7R2L6gNs

sanya:
Token eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoyMzEwMzYzMTk0LCJpYXQiOjE3MDYxNjc5OTQsImp0aSI6ImNiZWYyODdjYTVmOTRhNDJhZTEzMTRkNWJkZjcwNTk5IiwidXNlcl9pZCI6M30.XXsoUKw6BqSeW0FR_-nNjuC4wkYYtq816O1CbXxa4V0

oleg:
Token eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoyMzEwMzYzMjEyLCJpYXQiOjE3MDYxNjgwMTIsImp0aSI6ImNmYzMzNGJhMWM0MDRkODc4NDRiOTM0NGI4MjZkZjcwIiwidXNlcl9pZCI6NH0.XBGTYQwMPA8xJ_gZkqL6_SM4o4AAQ6Xdfw6gEMHf1PQ
            
///////////////////////////////////////////////////////////////////////////////////////////////////
account:
customuser: permissions, model, serializers, views, admin, urls +
customuser: phone, celery ?
vendor: start +


product:
category: model, serializers, views, admin, urls +
category: slug, mptt ?
category: fix unique preview
product: start++


config:
settings: fix jwt +


///////////////////////////////////////////////////////////////////////////////////////////////////

Reg. temple:

{
  "username": "andrey",
  "email": "user@example.com",
  "password": "stringst",
  "password2": "stringst"
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
