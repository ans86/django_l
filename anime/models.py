from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='author_images/')
    background_image = models.ImageField(upload_to="anime_backgrounds/", null=True, blank=True)  # 🔥 yaha background
    detail = models.TextField()

    def __str__(self):
        return self.name


class Anime(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='anime_images/')
    description = models.TextField()
    release_date = models.DateField()
    genre = models.CharField(max_length=50)
    rating = models.DecimalField(max_digits=3, decimal_places=1)

    # ForeignKey se Author ko connect kiya
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name="animes",
        default=1
    )

    def __str__(self):
        return self.title
