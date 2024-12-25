from django.shortcuts import render
from .models import CareerJourney, PhotoGallery, PhotoPrice, Service

# Create your views here.
def home(request):
    career_journeys = CareerJourney.objects.all() # mengambil semua data perjalanan karir
    photo_gallery = PhotoGallery.objects.all() # mengambil semua foto galeri
    photo_prices = PhotoPrice.objects.all() # mengambil semua harga per foto
    services = Service.objects.all() # mengambil semua layanan yang tersedia

    context = {
        'career_journeys': career_journeys,
        'photo_gallery': photo_gallery,
        'photo_prices': photo_prices,
        'services': services,
    }

    return render(request, 'home.html', context)

# tampilan untuk galeri
def gallery(request):
    photos = PhotoGallery.objects.all()
    context = {
        'photos': photos,
    }
    return render(request, 'gallery/galeri.html', context)

# Halaman Tentang Kami
def about(request):
    career_journeys = CareerJourney.objects.all()
    context = {
        'career_journeys': career_journeys,
    }
    return render(request, 'gallery/tentang_kami.html', context)

# Halaman Layanan
def services(request):
    services = Service.objects.all()
    context = {
        'services': services,
    }
    return render(request, 'gallery/layanan.html', context)

# Halaman Harga
def pricing(request):
    prices = PhotoPrice.objects.all()
    context = {
        'prices': prices,
    }
    return render(request, 'gallery/harga.html', context)
