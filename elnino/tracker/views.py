from django.shortcuts import render
from django.http import JsonResponse
from .models import Nino34Reading
# Create your views here.

def nino34_data(request):
    readings = Nino34Reading.objects.all().values("year", "month", "anomaly")
    return JsonResponse(list(readings), safe=False)

def dashboard(request):
    return render(request, "tracker/dashboard.html")