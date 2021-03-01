from django.db import models
import uuid

# Create your models here.

class Preson(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30)
    sex = models.BooleanField()
    phone = models.CharField(max_length=11)
    email = models.EmailField()
    country = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    status = models.CharField(max_length=100)
    img = models.ImageField(upload_to='user')



