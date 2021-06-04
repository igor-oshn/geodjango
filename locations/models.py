from django.db import models


class Company(models.Model):
    def __str__(self):
        return self.company_token

    company_token = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Device(models.Model):
    def __str__(self):
        return self.device_id

    company_id = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True)
    device_id = models.CharField(max_length=255, unique=True)
    device_model = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    app = models.CharField(max_length=255)
    version = models.CharField(max_length=255)


class Location(models.Model):
    def __str__(self):
        return "%s - %s" % (self.latitude, self.longitude)

    latitude = models.DecimalField(max_digits=11, decimal_places=9)
    longitude = models.DecimalField(max_digits=11, decimal_places=9)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    device_id = models.ForeignKey(Device, on_delete=models.CASCADE)
    data = models.JSONField(blank=True, null=True)
