from django.contrib import admin

from account.models import CustomUser, Vendor

admin.site.register(CustomUser)
admin.site.register(Vendor)
