from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = (
        ('Adhesive Sealants', 'Adhesive Sealants'),
        ('Locks', 'Locks'),
        ('Hinges', 'Hinges'),
        ('Shelf Support', 'Shelf Support'),
        ('Nails Staples', 'Nails Staples'),
        ('Screws', 'Screws'),
        ('Plumbing', 'Plumbing'),
        ('Tools', 'Tools'),
        ('Abrasives', 'Abrasives'),
        ('Fasteners', 'Fasteners'),
        ('Locks', 'Locks'),
        ('Cleaning Supplies', 'Cleaning Supplies'),
        ('Paint', 'Paint'),
        ('Hardware', 'Hardware'),
        ('Misc', 'Misc'),
    )
    brand = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200, null=True)
    sku = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    finishes = models.CharField(max_length=200, null=True, blank=True)
    category_name = models.CharField(choices=CATEGORY_CHOICES, default=CATEGORY_CHOICES[0], max_length=200, null=True)
    is_in_stock = models.BooleanField(verbose_name='Is in stock?', default=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ""
        return url
