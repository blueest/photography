from django.contrib import admin
from .models import CareerJourney, PhotoGallery, PhotoPrice, Service

@admin.register(CareerJourney)
class CareerJourneyAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_started', 'date_ended')
    search_fields = ('title', 'description')
    list_filter = ('date_started', 'date_ended')

@admin.register(PhotoGallery)
class PhotoGalleryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title', 'description')

@admin.register(PhotoPrice)
class PhotoPriceAdmin(admin.ModelAdmin):
    list_display = ('category', 'price')
    search_fields = ('category',)
    list_filter = ('category',)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'whatsapp_number')
    search_fields = ('name', 'description', 'whatsapp_number')
