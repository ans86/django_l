from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Authors(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to="authors/")
    dateofbirth = models.CharField(max_length=255)
    publishedbooks = models.IntegerField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True)
    

    def __str__(self):
        return self.name



class Book(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="books/")
    author = models.CharField(max_length=255)
    publishyear = models.IntegerField()
    author = models.ForeignKey(Authors, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title

