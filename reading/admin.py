from django.contrib import admin
from reading.models import House, Reading, Tenant, YearlyBill

admin.site.register(House)
admin.site.register(Tenant)
admin.site.register(YearlyBill)
admin.site.register(Reading)
