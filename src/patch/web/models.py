from django.db import models
import uuid

FAQ_TYPE = (
   ("rent_tracking","Rent Tracking"),
   ("new_deposit","New Deposit"),
   ("existing_deposit","Existing Deposit")
)


class Testimonial(models.Model):
   name = models.CharField(max_length=255)
   designation = models.CharField(max_length=255,default="Software engineer")
   image= models.ImageField(upload_to="testimonials/")
   description = models.TextField(blank=True,null=True)
   dob = models.DateTimeField(blank=True,null=True)
   #dob = models.DateField(blank=True,null=True)
   #dob = models.TimeField(blank=True,null=True)

   def __str__(self):
      return self.name
   

class Promoter(models.Model):
   name= models.CharField(max_length=255)
   image= models.ImageField(upload_to="promoters/")

   def __str__(self):
      return self.name
   

class Faq(models.Model):
   title = models.CharField(max_length=255)
   description = models.TextField()
   faq_type = models.CharField(max_length=128,choices=FAQ_TYPE)

   def __str__(self):
      return self.title


class Subscribe(models.Model):
   email = models.EmailField(unique=True)
   #created_time = models.DateTimeField(auto_now_add=True)

   def __str__(self):
      return self.email


#class TestModel(models.Model):
   #id = models.BigAutoField()
   #id = models.BigIntegerField()
   #id = models.FloatField()
   #id = models.DecimalField(max_digits=..,decimal_places=..)

   #is_student = models.BooleanField(default=True)

   #document = models.FileField(upload_to="documents/")

   #id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)