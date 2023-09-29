from rest_framework import serializers
from .models import *


class FilmSerializers(serializers.ModelSerializer):

    class Meta:
        model = Film
        fields = '__all__'

# class FilmSerializers(serializers.Serializer):
#     poster = serializers.ImageField(use_url='poster.url')
#     title_ru = serializers.CharField(max_length=255)
#     title_orig = serializers.CharField(max_length=255)
#     prod_year = serializers.IntegerField()
#     timing = serializers.IntegerField()
#     premiere_date = serializers.DateField()
#     country_id = serializers.IntegerField()
#     genre_id = serializers.IntegerField()
#     director_id = serializers.IntegerField()    


#     def create(self, validated_data):
#         return Film.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.poster = validated_data.get('poster', instance.poster)
#         instance.title_ru = validated_data.get('title_ru', instance.title_ru)
#         instance.title_orig = validated_data.get('title_orig', instance.title_orig)
#         instance.prod_year = validated_data.get('prod_year', instance.prod_year)
#         instance.timing = validated_data.get('timing', instance.timing)
#         instance.premiere_date = validated_data.get('premiere_date', instance.premiere_date)
#         instance.country_id = validated_data.get('country', instance.country_id)
#         instance.genre_id = validated_data.get('genre', instance.genre_id)
#         instance.director_id = validated_data.get('director', instance.director_id)

#         instance.save()
#         return instance
