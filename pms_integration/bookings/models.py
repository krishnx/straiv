from django.db import models


class Booking(models.Model):
    booking_id = models.CharField(max_length=100, unique=True)
    guest = models.CharField(max_length=255)
    room_number = models.CharField(max_length=20)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    misc = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.guest} ({self.booking_id})"
