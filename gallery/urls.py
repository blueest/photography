from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Halaman utama
    path('gallery/', views.gallery, name='gallery'),  # Halaman galeri
    path('about/', views.about, name='about'),  # Halaman tentang kami
    path('services/', views.services, name='services'),  # Halaman layanan
    path('pricing/', views.pricing, name='pricing'),  # Halaman harga
]
