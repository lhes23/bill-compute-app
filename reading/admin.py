from django.contrib import admin

from reading.models import House, Reading, Tenant

admin.site.register(House)
admin.site.register(Tenant)
admin.site.register(Reading)
