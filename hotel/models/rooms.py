from django.db import models
from hotel.models.hotels import Hotel

class Room(models.Model):
    RoomID = models.IntegerField()
    Hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='rooms')
    RoomType = models.CharField(max_length=50)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Availability = models.BooleanField()
    Features = models.TextField()

    class Meta:
        unique_together = ('RoomID', 'Hotel')

    def __str__(self):
        return f"{self.Hotel.Name} - Room {self.RoomID}"