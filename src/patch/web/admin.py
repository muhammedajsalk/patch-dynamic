from django.contrib import admin
from web.models import Testimonial


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ["id","name","designation","description"]


admin.site.register(Testimonial,TestimonialAdmin)
