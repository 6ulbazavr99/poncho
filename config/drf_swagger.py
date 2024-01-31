from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Poncho API",
      default_version='v1',   # TODO:
      description="""

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

+admin[1:1]:
Token eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoyMzEwODk0MjE3LCJpYXQiOjE3MDY2OTkwMTcsImp0aSI6ImYwNGU0ZmE4NDA4YTQ4M2NiZmVhM2NiMjhkNzZkYzI3IiwidXNlcl9pZCI6MX0.mzi9moO3jZR41Jwh4Svq2Yf1dxqYIBVZcs4CYA_rBHw

andrey[2:bastard123]:
Token eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoyMzEwNjY4NTY3LCJpYXQiOjE3MDY0NzMzNjcsImp0aSI6ImI1Yjc5OTY3NWYyNTRjYWRhZjQyYWJhNWRlMzIwNjYxIiwidXNlcl9pZCI6Mn0.01zlLAguGtrN7newNkEON1wDHisR5LZpxf_zEBBkncU

user1:
Token eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoyMzEwNTk1ODg5LCJpYXQiOjE3MDY0MDA2ODksImp0aSI6IjQ5MThhMTNiNTU5ZDQyZTk5YjU4NTNmOGZmMGQyNzYzIiwidXNlcl9pZCI6M30.XRHBmX0kykecvJGw23CSbmpEwArkyE_b87qLZHYDQCI

user2:
Token eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoyMzEwNTk1OTg3LCJpYXQiOjE3MDY0MDA3ODcsImp0aSI6ImM1MTFhM2NlZjg5MTRhN2ZiOGM5NmEzNTBkOThhZjRhIiwidXNlcl9pZCI6NH0.dYzIrQ6L--4v0Y3l6z0I_K_EvBB1oOPouEW32HjCf58
            
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#
#
#
############### <account:
customuser: permissions, model, serializers, views, admin, urls +
customuser: phone, celery ?
vendor: start +
vendor: 80% +
customuser: 80% +
signals: celery ?
vendor&user: fix sers&perms +
user: reg email confirmation + 
user/utils: change host !!!
user: 80% +
vendor: 80% +
user: reset password +
user: is_active superuser fix +
vendor: fix head adding to members !!!!!!
############### :account>
#
#
#
############### <product:
category: model, serializers, views, admin, urls +
category: slug, mptt ?
category: fix unique preview -
product: start +
product: 70% +
product: sers +
category: products list GET ID +
category: add listing ser +
category: 80% +
product: 80% +
product: vendor require
############### :product>
#
#
#
############### <order:
order: fix amount
orderitem: fix amount
############### :order>
#
#
#
############### <config:
settings: fix jwt +
settings: emailback +
drf_swagger: new schema add +
############### :config>
#
#
#
############### <general:
formatting the code +
emailback +
db_diagram +
db_duagram: fix 
############### :general>
#
#
#
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#
#
#
############### <registration:
#
{"username": "user",
"email": "user@gmail.com",
"password": "bastard123",
"password_confirmation": "bastard123"}
#
############### :registration>
#
#
#
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#
#
#
      """,
      terms_of_service="https://github.com/bulka174/poncho",
      license=openapi.License(name="↑ GitHub ↑"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
   path('docs<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redocs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
