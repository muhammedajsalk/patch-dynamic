from django.contrib import admin
from web.models import Testimonial,Promoter,Faq,Subscribe,Car,Manufacturer


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ["id","name","designation","image","description"]

admin.site.register(Testimonial,TestimonialAdmin)


class PromoterAdmin(admin.ModelAdmin):
    list_display = ["id","name","image"]

admin.site.register(Promoter,PromoterAdmin)


class FaqAdmin(admin.ModelAdmin):
    list_display = ["id","title","description","faq_type"]

admin.site.register(Faq,FaqAdmin)


admin.site.register(Subscribe)

admin.site.register(Car)
admin.site.register(Manufacturer)
