from django.shortcuts import render
from . import models

def index(request):
    return render(request, "index.html", {
        "sentence": models.Sentence.objects.order_by("?").first()
    })
