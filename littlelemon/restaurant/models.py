from django.db import models

class Menu(models.Model):
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Inventory = models.SmallIntegerField(default=6)
    
    def __str__(self):
        return self.Title
    



class Booking(models.Model):
    Name = models.CharField(max_length=255)
    No_of_guests = models.SmallIntegerField(default=6)
    Booking_date = models.DateTimeField()
    
    def __str__(self):
        return self.Name
