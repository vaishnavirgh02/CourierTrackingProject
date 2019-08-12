from django.db import models
from django.contrib.auth.models import User


class Office(models.Model):
    office_name = models.CharField(max_length=30, unique = True)
    office_code = models.CharField( max_length=6, unique = True)
    office_address = models.TextField(max_length= 150)
    office_pincode = models.IntegerField(unique = True)

    def __str__(self):
        return f'{ self.office_code } {self.office_pincode}'



# Create your models here.
class Consignment(models.Model):
    CONSIGNMENT_TYPE = [('Letter', 'Letter')]
    PACKAGE_SIZE = [('S', 'Small'), ('M', 'Medium'), ('L', 'Large')]
    SERVICE_TYPE = [('Premium', 'Premium'), ('Overnight', 'Overnight'), ('Regular', 'Regular')]

    consignment_sender = models.ForeignKey(User, on_delete=models.CASCADE)
    consignment_name = models.CharField(max_length = 30)
    material = models.CharField(max_length = 30, choices=CONSIGNMENT_TYPE)
    package_size = models.CharField(max_length = 30, choices=PACKAGE_SIZE)
    service_type = models.CharField(max_length = 30, choices=SERVICE_TYPE)
    service_price = models.DecimalField(max_digits=10, decimal_places=2)
    weight_in_gm = models.DecimalField(max_digits=10, decimal_places=2)
    consignment_source = models.ForeignKey(Office, on_delete=models.PROTECT, related_name = 'source')
    consignment_destination = models.ForeignKey(Office, on_delete=models.PROTECT, related_name = 'destination')
    consignment_address = models.TextField(max_length= 150)

    def __str__(self):
        return f'{ self.consignment_name }'



class Transporter(models.Model):
    name = models.CharField(max_length = 30)
    phone_no = models.CharField(max_length = 30)

    def __str__(self):
        return f'{ self.name }'

        

class DeliveryProgress(models.Model):
    EVENT = [('RECIEVED', 'Recieved'), ('DISPATCHED', 'Dispatched')]

    consignment = models.ForeignKey(Consignment, on_delete=models.CASCADE)
    hub = models.ForeignKey(Office, on_delete=models.PROTECT, related_name = 'hub')
    event = models.CharField(max_length = 30, choices=EVENT)
    transporter = models.ForeignKey(Transporter, on_delete=models.PROTECT)
    
    def __str__(self):
        return f'{ self.consignment }'
