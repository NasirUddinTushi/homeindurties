from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    parent = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.SET_NULL, related_name='children'
    )
    image = models.ImageField(upload_to='category_images/', null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.parent and self.parent.id == self.id:
            raise ValueError("Category cannot be parent of itself")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Attribute(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class AttributeValue(models.Model):
    attribute = models.ForeignKey(Attribute, related_name='values', on_delete=models.CASCADE)
    value = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.attribute.name}: {self.value}"


class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    is_bestseller = models.BooleanField(default=False)
    is_new = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    short_description = models.TextField(blank=True)
    attributes = models.ManyToManyField(AttributeValue, blank=True)  # ✅ final

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return f"Image for {self.product.name}"
