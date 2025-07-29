from django.db import models

class Contact(models.Model):
     name = models.CharField(max_length=255)
     username = models.CharField(max_length=100)  # New field
     email = models.EmailField()
     message = models.TextField()
     timeStamp = models.DateTimeField(auto_now_add=True)

     def __str__(self):
          return "Message from " + self.name + ' - ' + self.email