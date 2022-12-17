from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from django.urls import path

from . import views
from songs import views as song_views

urlpatterns = [
    path("albums/", views.AlbumView.as_view()),
    path("albums/<int:pk>/songs/", song_views.SongView.as_view()),

    # Doc
    # Acessa o download do schema
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    # Opcionais
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
