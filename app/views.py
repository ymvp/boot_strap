from django.shortcuts import render

# Create your views here.
def download_bootstrap(request):
    return render(request,'download_bootstrap.html')