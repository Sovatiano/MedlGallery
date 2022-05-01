from django.urls import path
from . import views


urlpatterns = [
    path('gallery/', views.gallery, name='gallery'),
    path('image/<str:pi>', views.image, name='image'),
    path('cabinet/', views.cabinet, name='cabinet'),
    path('search/<str:filter>', views.search, name='searchfilter'),
    path('search/', views.search, name='search')
]