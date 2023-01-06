
from django.db import models


class Artist(models.Model):
    name = models.TextField()
    def __str__(self):
        return f"{self.name}"

class Album(models.Model):
    title = models.TextField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.title} - {self.artist.name}"
    
class Track(models.Model):
    name = models.TextField()
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=4)
    
    def __str__(self):
        return f"{self.name}"