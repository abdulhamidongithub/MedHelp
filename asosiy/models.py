from django.db import models

class Mijoz(models.Model):
    ism = models.CharField(max_length=50)
    tugilgan_yil = models.PositiveSmallIntegerField()
    vaqt = models.DateTimeField(auto_now_add=True)
    tel_raqam = models.CharField(max_length=20)
    faol = models.BooleanField(default=True)
    longlitude = models.CharField(max_length=30)
    latitude = models.CharField(max_length=30)
    geolocation_url = models.CharField(max_length=300, blank=True)
    def __str__(self):
        return f"{self.ism} ({self.vaqt})"

    def save(self, *args, **kwargs):
        self.geolocation_url = f"https://www.google.com/maps/search/?api=1&query={self.latitude},{self.longlitude}"
        super().save(*args, **kwargs)


