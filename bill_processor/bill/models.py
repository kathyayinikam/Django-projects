from django.db import models
from django.db import models

class Bill(models.Model):
    image = models.ImageField(upload_to='bills/')
    rr_number = models.CharField(max_length=100, blank=True)
    account_id = models.CharField(max_length=100, blank=True)
    consumption = models.CharField(max_length=100, blank=True)
    tax = models.CharField(max_length=100, blank=True)
    net_amount_due = models.CharField(max_length=100, blank=True)
    processed = models.BooleanField(default=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)

# Create your models here.
