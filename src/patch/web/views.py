from django.shortcuts import render
from web.models import Testimonial


def index(request):
    testimonials=Testimonial.objects.all()

    print(testimonials)
    
    context={
        "testimonials": testimonials
    }
    return render(request,"index.html",context=context)
