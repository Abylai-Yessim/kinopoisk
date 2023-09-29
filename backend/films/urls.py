from django.urls import path, include 
from rest_framework.routers import SimpleRouter
from . import views 

# router = SimpleRouter()
# router.register(r'', views.FilmViewSet)

app_name = 'films'

urlpatterns = [
    # path('', include(router.urls)),
    path('', views.FilmListAPIView.as_view()),
    path('<int:pk>/', views.FilmDetailAPIView.as_view()),
    path('auth/', include('rest_framework.urls')),
    # path('', views.FilmViewSet.as_view({'get': 'list'})),
    # path('<int:pk>/', views.FilmViewSet.as_view({'get': 'retrieve'}))
]