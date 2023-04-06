from django.db import models


# Create your models here.

class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    firest_name = models.CharField(max_length=50,)
    last_name = models.CharField(max_length=50,)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=20,blank=True)
    address = models.CharField(max_length=50,)
    city = models.CharField(max_length=50,)
    state = models.CharField(max_length=50,)
    zip_code = models.IntegerField()
    
    def __str__(self):
        return (f"{self.firest_name} {self.last_name}")
    