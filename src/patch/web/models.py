from django.db import models


class Testimonial(models.Model):
   name = models.CharField(max_length=255)
   designation = models.CharField(max_length=255)
   description = models.TextField()