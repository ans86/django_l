from django.db import models

class Game(models.Model):
     name= models.CharField(max_length=255)
     image = models.ImageField(upload_to="games/")
     message = models.TextField()
     timeStamp = models.DateTimeField(auto_now_add=True)


     
     def _str_(self):
          return "Message from " + self.name + ' - ' + self.email