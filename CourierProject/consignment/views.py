from django.shortcuts import render

# Create your views here.
def Index(request):
    return render(request, 'consignment/index.html')


def Dashboard(request):
    return render(request, 'consignment/dashboard.html')
