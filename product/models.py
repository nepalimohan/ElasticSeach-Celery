from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    description = models.TextField()
    
    class Meta:
        ordering = ['-id']
        verbose_name_plural = 'Products'
        
    
    def __str__(self):
        return f"{self.name} | {self.category}"
    