from django.db import models

class Hotel(models.Model):
    HotelID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    Location = models.CharField(max_length=255)
    Description = models.TextField()
    StarRating = models.IntegerField()
    Amenities = models.TextField()
    ContactInfo = models.CharField(max_length=255)

    def __str__(self):
        return self.Name