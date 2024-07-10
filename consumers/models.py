from django.db import models

class Consumer(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    contact_details = models.CharField(max_length=255)

    def __str__(self):
        return self.name
