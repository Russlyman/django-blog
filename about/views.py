from django.shortcuts import render, get_object_or_404
from .models import About
from .forms import CollaborateRequestForm

# Create your views here.
def about_view(request):
    about = About.objects.all().order_by('-updated_on').first()

    collaborate_form = CollaborateRequestForm()

    return render(
        request,
        "about/index.html",
        {"about": about, "collaborate_form": collaborate_form},
    )