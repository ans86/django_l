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
        return f"{self.name} - {self.model}"