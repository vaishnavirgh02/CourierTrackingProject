from django import forms
from .models import Consignment, DeliveryProgress

class ConsignmentRegisterForm(forms.ModelForm):
    class Meta():
        model = Consignment
        fields = ['consignment_sender','consignment_name', 'material', 'package_size', 'service_type', 'service_price' ,  'weight_in_gm', 'consignment_source', 'consignment_destination', 'consignment_address']

class ConsignmentUpdateForm(forms.ModelForm):
    class Meta():
        model = DeliveryProgress
        fields = ['consignment','hub', 'event', 'transporter']