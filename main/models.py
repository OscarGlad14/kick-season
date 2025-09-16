import uuid
from django.db import models
from django.utils.timezone import now

# Create your models here.
class Product(models.Model):
    CATEGORY_CHOICES = [
        ('sepatu', 'Sepatu'),
        ('pakaian', 'Pakaian'),
        ('aksesoris', 'Aksesoris')
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    thumbnail = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(default=now)
    name = models.CharField(max_length=255)
    description = models.TextField(default="")
    price = models.IntegerField(default=0)
    category = models.CharField(max_length=255, choices=CATEGORY_CHOICES, default='sepatu')
    product_views = models.PositiveIntegerField(default=0)
    is_featured = models.BooleanField(default=False)
    stock = models.IntegerField(default=0)
    brand = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
    def increment_views(self):
        self.product_views += 1
        self.save()