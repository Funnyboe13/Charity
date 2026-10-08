from django.db import models  
class Activity(models.Model):
   title = models.CharField(max_length=200) 
   description = models.TextField(blank=True) 
   date = models.DateField() 
   category = models.CharField(max_length=100, blank=True) 
   hours = models.DecimalField(max_digits=6, decimal_places=1, default=0) 
def __str__(self): 
    return self.title
class Volunteer(models.Model): 
   name = models.CharField(max_length=150) 
   email = models.EmailField(blank=True) 
   total_hours = models.DecimalField(max_digits=6, decimal_places=1, default=0) 
def __str__(self): 
   return self.name 
class Donation(models.Model): 
   user = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, blank=True)
   donor_name = models.CharField(max_length=150, default="Anonymous") 
   phone_number = models.CharField(max_length=20, blank=True)
   amount = models.DecimalField(max_digits=10, decimal_places=2) 
   date = models.DateField(auto_now_add=True) 
   purpose = models.CharField(max_length=200, blank=True) 
   status = models.CharField(
    max_length=20,
    choices=[
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('failed', 'Failed'),
    ],
    default='confirmed'
)
def __str__(self): 
   return f"{self.donor_name} - {self.amount}"


# Create your models here.
