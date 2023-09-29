from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators  import action 
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import *
from .serializers import *
from .permissions import *


# Create your views here.
class FilmListAPIView(ListCreateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializers
    # permission_classes = (IsAdminOrReadOnly, )



class FilmDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializers
    # permission_classes = (IsAdminOrReadOnly, )


# class FilmViewSet(ModelViewSet):
#     queryset = Film.objects.all()
#     serializer_class = FilmSerializers

    
#     @action(methods=['get'], detail=False)
#     def genres(self, request):
#         genres = Genre.objects.all()
#         return Response([genre.name for genre in genres])
    
#     @action(methods=['get'], detail=False)
#     def genre_filter(self, request):
#         films = Film.objects.filter(genre_id=self.request.query_params.get('genre_id'))
#         serializer = FilmSerializers(films, many=True)
#         return Response(serializer.data)




# class FilmListAPIView(ListCreateAPIView):
#     queryset = Film.objects.all()
#     serializer_class = FilmSerializers

# class FilmDetailAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Film.objects.all()
#     serializer_class = FilmSerializers




class FilmAPIView(APIView):
    def get(self, request):
        films = Film.objects.all()
        return Response({'films': FilmSerializers(films, many=True).data})
    
    def post(self, request):

        # new_film = Film.objects.create(
        #     poster=request.data['poster'],
        #     title_ru=request.data['title_ru'],
        #     title_orig=request.data['title_orig'],
        #     prod_year=request.data['prod_year'],
        #     timing = request.data['timing'],
        #     premiere_date = request.data['premiere_date'],
        #     country_id = request.data['country_id'],
        #     genre_id = request.data['genre_id'],
        #     director_id = request.data['director_id'],
        # )
        # new_film.save()

        # return Response({'films': FilmSerializers(new_film).data})

        serializers = FilmSerializers(data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()

        return Response({'films': serializers.data})
    
    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)

        if not pk:
            return Response({'error': 'Method "PUT" not allowed.'})
        
        try:
            instance = Film.objects.get(pk=pk)
        except:
            return Response({'error': 'Object does not exists.'})
        
        serializers = FilmSerializers(data=request.data, instance=instance)
        serializers.is_valid(raise_exception=True)
        serializers.save()

        return Response({'films': serializers.data})
    
    
    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)

        if not pk:
            return Response({'error': 'Method "DELETE" not allowed.'})
         
        try:
            instance = Film.objects.get(pk=pk)
            instance.delete()
        except:
            return Response({'error': 'Object does not exists.'})

        return Response({'status': 'Film was deleted'})
    
   


