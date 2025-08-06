from django.db import models

class Laptop(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="Laptops/")
    details = models.TextField()
    generation = models.TextField()
    ram = models.PositiveIntegerField(help_text="RAM in GB")
    ssd = models.PositiveIntegerField(help_text="SSD in GB")
    timeStamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Laptop Entry: {self.name} | {self.ram}GB RAM, {self.ssd}GB SSD"