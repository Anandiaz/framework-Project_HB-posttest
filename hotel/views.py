from django.shortcuts import render
from django.conf import settings

# Create your views here.
def homepage(request):
    return render(request, "homepage/index.html")

# Verify the MEDIA_URL to all templates
def media_url_processor(request):
    return{
        "MEDIA_URL" : settings.MEDIA_URL,
    }