from django.db import models

class CylinderType(models.Model):
    name = models.CharField(max_length=255)
    capacity = models.IntegerField()

    def __str__(self):
        return self.name

class Cylinder(models.Model):
    STATUS_CHOICES = [
        ('empty', 'Empty'),
        ('full', 'Full')
    ]

    type = models.ForeignKey(CylinderType, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    location = models.CharField(max_length=255)
    consumer = models.ForeignKey('consumers.Consumer', on_delete=models.SET_NULL, null=True, blank=True)
    refill_center = models.ForeignKey('refill_centers.RefillCenter', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.type.name} - {self.status}'
