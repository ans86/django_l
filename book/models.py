from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="books/")
    author = models.CharField()
    publishyear = models.IntegerField()

    def __str__(self):
        return self.title


# class Author(models.Model):
#     book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="authors")
#     name = models.CharField(max_length=300)
#     image = models.ImageField(upload_to="authors/")
#     fathername = models.CharField(max_length=255)
#     publishedbooks = models.IntegerField()

#     def __str__(self):
#         return self.name
