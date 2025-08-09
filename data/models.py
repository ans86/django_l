from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  # Link to Author
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="books/")
    publishyear = models.IntegerField()

    def __str__(self):
        return self.name
