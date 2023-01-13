from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from django.db import models


class Artist(models.Model):
    name = models.TextField()
    
    def __str__(self):
        return f"{self.name}"

class Album(models.Model):
    title = models.TextField()
    artist_id = models.ForeignKey(Artist, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.title}, {self.artist_id.name}"

class Track(models.Model):
    name = models.TextField(validators=[RegexValidator(
        regex=r"^[a-zA-Z0-9]{6}$",
        code="invalid",
        message="No"
    )])
    album_id = models.ForeignKey(Album, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=10, validators=[MinValueValidator(1)])
    
    def __str__(self):
        return f"{self.name}"