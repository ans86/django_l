from django.db import models

class Game(models.Model):
     name= models.CharField(max_length=255)
     image=models.ImageField( upload_to=None, height_field=None, width_field=None, max_length=None)
     message = models.TextField()
     timeStamp = models.DateTimeField(auto_now_add=True)


     
     def _str_(self):
          return "Message from " + self.name + ' - ' + self.email