from django.contrib import admin

from music.models import Artist, Album, Track

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    pass

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    pass

@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', "album")
    
    