from django.db import models

class Airline(models.Model):
    name = models.CharField(max_length=100)
    digit_code = models.CharField(max_length=2)
    three_digit_code = models.CharField(max_length=3)
    country = models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.digit_code}:{self.name}"


class Airport(models.Model):
    name = models.CharField(max_length=250)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    code = models.CharField(max_length=3)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.code}:{self.name}"

class Route(models.Model):
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="origin")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="destination")
    
    def __str__(self):
        return f"{self.airline.name}:{self.origin.code}-{self.destination.code}"