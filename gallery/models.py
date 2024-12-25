from django.db import models

# Create your models here.
class CareerJourney(models.Model):
    title = models.CharField(max_length=225)
    description = models.TextField()
    date_started = models.DateField()
    date_ended = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title
    
class PhotoGallery(models.Model):
    title = models.CharField(max_length=225)
    image = models.ImageField(upload_to='gallery')
    description = models.TextField()

    def __str__(self):
        return self.title
    
class PhotoPrice(models.Model):
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=0)

    def __str__(self):
        return f"{self.category} - {self.price}"
    
class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    whatsapp_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name
