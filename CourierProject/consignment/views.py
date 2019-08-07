from django.shortcuts import render

# Create your views here.
def Index(requests):
    return render(request, 'consignment/index.html')
