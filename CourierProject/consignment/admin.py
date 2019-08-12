from django.contrib import admin
from .models import Office, Consignment, DeliveryProgress, Transporter

# Register your models here.
admin.site.register(Consignment)
admin.site.register(Office)
admin.site.register(DeliveryProgress)
admin.site.register(Transporter)
