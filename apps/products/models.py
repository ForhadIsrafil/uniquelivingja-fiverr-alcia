from django.db import models


class Product(models.Model):
    MAIN_CATEGORY_CHOICES = (
        ('Bathroom', 'Bathroom'),
        ('Kitchen', 'Kitchen'),
        ('Commercial', 'Commercial'),
        ('Hardware', 'Hardware'),
    )
    SUB_CATEGORY_CHOICES = (
        ('Accessories', 'Accessories'),
        ('Showers', 'Showers'),
        ('Basin-Faucets', 'Basin-Faucets'),
        ('Toilets', 'Toilets'),
        ('Lighting', 'Lighting'),
    )
    SUB_SUB_CATEGORY_CHOICES = (
        ('Accessories', 'Accessories'),
        ('Showers', 'Showers'),
        ('Basin-Faucets', 'Basin-Faucets'),
        ('Toilets', 'Toilets'),
        ('Lighting', 'Lighting'),
    )
    brand = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200, null=True)
    sku = models.CharField(max_length=200, null=True, blank=True)
    # description = models.TextField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    image = models.ImageField(upload_to='product_images',null=True, blank=True)
    finishes = models.CharField(max_length=200, null=True, blank=True)
    # featured = models.BooleanField(default=False) will added if needed
    main_category = models.CharField(choices=MAIN_CATEGORY_CHOICES, default=MAIN_CATEGORY_CHOICES[0], max_length=200,
                                     null=True)
    sub_category = models.CharField(choices=SUB_CATEGORY_CHOICES, default=SUB_CATEGORY_CHOICES[0], max_length=200,
                                    null=True)
    sub_sub_category = models.CharField(choices=SUB_SUB_CATEGORY_CHOICES, default=SUB_SUB_CATEGORY_CHOICES[0],
                                        max_length=200,
                                        null=True)
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


class HomeSlider(models.Model):
    HOME_SLIDER_CHOICES = (
        ('/category/kitchen', '/category/kitchen'),
        ('/category/bathroom', '/category/bathroom'),
        ('/category/commercial', '/category/commercial'),
    )

    image = models.ImageField(upload_to='home_slider', null=True, blank=True)
    category_url = models.CharField(max_length=200, choices=HOME_SLIDER_CHOICES, default=HOME_SLIDER_CHOICES[0],
                                    null=True, blank=True)

    def __str__(self):
        return self.image.url
