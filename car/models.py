from django.db import models

class Car(models.Model):
     name = models.CharField(max_length=255)
     image = models.ImageField(upload_to="cars/")
     model = models.TextField()
     engine = models.TextField()
     enginepower = models.TextField()
     price = models.TextField()
     madein = models.TextField()
     topspeed = models.TextField()

     def __str__(self):
        return f"{self.name}"
     
class Review(models.Model):
     name = models.CharField(max_length=255, null=True, blank=True)
     review = models.CharField(max_length=255, null=True, blank=True)
     rating = models.IntegerField(default=0)
     car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='reviews')
     review = models.TextField(null=True, blank=True)
     

def __str__(self):
        return f"{self.name} -{self.review}  -{self.car}"