from django.db import models
from django.utils import timezone


class Officer(models.Model):
    firstName = models.TextField()
    lastName = models.TextField()
   


    def __getOfficerName__(self):
        return self.firstName