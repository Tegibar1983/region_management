from django.shortcuts import render
from .models import RegionalInfo

# Create your views here.

def home(request):
    all_regions=RegionalInfo.objects.all()
    context={'all_regions':all_regions}
    return render(request, 'home.html', context=context)