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
Token eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoyMzEwNTU5NzQ1LCJpYXQiOjE3MDYzNjQ1NDUsImp0aSI6IjI1NjNjMDJjM2Y4ODQ5Yjg5M2E2ZWM3YWQwNDE4OTBjIiwidXNlcl9pZCI6MX0.hPxZt5bLmHeKX8ooWjQY938Cq_nOcd6EK9E8l_Wgwu8

andrey:
Token eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoyMzEwNTU5NzY0LCJpYXQiOjE3MDYzNjQ1NjQsImp0aSI6ImIyMGE2YTgwYzU2NzQxMDY4M2FiNDIxNjVhODBiMjI5IiwidXNlcl9pZCI6Mn0.eV0L4QHdXmiDeYG4p4H4Zhdt1MGqnSRCcCcpgk7M96o

sanya:
Token eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoyMzEwNTU5NzgwLCJpYXQiOjE3MDYzNjQ1ODAsImp0aSI6IjQ3NWQ1NjA2NmJjNDRkM2FhMzlmNjU5OWQ5YTY2MWQ2IiwidXNlcl9pZCI6M30._F8Qq8yEa5E9Rq2SFyjFW4eh2Xy2D1dl-6jmXYMS_Ck

oleg:
Token eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoyMzEwNTU5Nzk2LCJpYXQiOjE3MDYzNjQ1OTYsImp0aSI6IjgwZGFmY2VkOGI1NTRkZWJhZGY3MTc4NTg0NWEyZTlkIiwidXNlcl9pZCI6NH0.e34_i55m9OjL-gb1ELcBp9G7n2maYZM2IUnUKpG5BMI
            
///////////////////////////////////////////////////////////////////////////////////////////////////
#
### account:
customuser: permissions, model, serializers, views, admin, urls +
customuser: phone, celery ?
vendor: start +
vendor: 80% +
customuser: 80% +
signals: celery ?
vendor&user: fix sers&perms +
#
### product:
category: model, serializers, views, admin, urls +
category: slug, mptt ?
category: fix unique preview
product: start +
product: 70% +
product: sers
category: products list GET ID +
category: add listing ser +
#
### config:
settings: fix jwt +
#
### general:
formatting the code +
#
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
