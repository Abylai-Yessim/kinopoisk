from django.db import models
import uuid
import os

def uniq_name_upload(instance, filename):
    new_file_name = f"{uuid.uuid4()}.{filename.split('.')[-1]}"
    return f'posters/{new_file_name}'

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

class Genre(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
    
class Director(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
class Film(models.Model):
    poster = models.ImageField(blank=True, upload_to=uniq_name_upload)
    title_ru = models.CharField(max_length=255)
    title_orig = models.CharField(max_length=255)
    prod_year = models.IntegerField()
    timing = models.IntegerField()
    premiere_date = models.DateField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)    


    def __str__(self):
        return self.title_orig
    
    def delete(self, *args, **kwargs):
        if self.poster and os.path.isfile(self.poster.path):
            os.remove(self.poster.path)

        super().delete(*args, **kwargs)
    


