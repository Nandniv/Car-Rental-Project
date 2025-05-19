from django.db import models
from django.utils import timezone
timezone.now()

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=30)
    email=models.EmailField()
    mobile=models.BigIntegerField()
    password=models.CharField(max_length=20)
    profile = models.ImageField(default="")
    usertype = models.CharField(max_length=20,default="customer")
    
    def __str__(self): #for printing object
        return self.name
    
class Car(models.Model):
    lessor = models.ForeignKey(User,on_delete=models.CASCADE)
    
    transmission = (
        
        ("Manual","Manual"),
        ("Auto","Auto")
    )
    fuel = (

        ("CNG","CNG"),
        ("Petrol","Petrol"),
        ("Diesel","Diesel")
    )
    sfuel = models.CharField(max_length=50,choices=fuel)
    stransmission = models.CharField(choices=transmission,max_length=50)
    cname = models.CharField(max_length=100)
    cprice = models.IntegerField(null=True, blank=True)
    cimage = models.ImageField(default="")
    mileage = models.IntegerField(null=True, blank=True)
    seats = models.IntegerField() 
    luggage = models.CharField(max_length=100, null=True, blank=True)
    desc = models.TextField(null=True, blank=True)     

    def __str__(self): #for printing object
        return self.cname
    
class Review(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.name} - {self.car.cname}"

class Booking(models.Model):
    STATUS_CHOICES = (
        (True, 'Confirmed'),
        (False, 'Pending'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    pickup_address=models.TextField()
    drop_address=models.TextField()
    pick_time=models.TimeField()
    total_days = models.IntegerField()
    total_amount = models.IntegerField()
    status = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.user.name} - {self.car.cname} ({self.start_date} - {self.end_date})"



def save(self, *args, **kwargs):
        # Calculate total days and amount
        if self.start_date and self.end_date:
            self.total_days = (self.end_date - self.start_date).days
            self.total_amount = self.total_days * self.car.cprice
        super().save(*args, **kwargs)
        
        
def __str__(self):
         return f"Booking #{self.id} - {self.car.cname}"