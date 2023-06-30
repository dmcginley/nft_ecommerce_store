from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify


class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(is_active=True)


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = "categories"

    def get_absolute_url(self):
        return reverse('board_app:category_list', args=[self.slug])

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Product(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True, upload_to='product_pics')
    description = models.CharField(max_length=300)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="post_author")

    stripe_product_id = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250, unique=True)
    date_posted = models.DateTimeField(default=timezone.now, editable=False)
    category = models.ForeignKey(
        Category, related_name='product', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    products = ProductManager()

    class Meta:
        ordering = ('-date_posted',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('store:product_detail', kwargs={'slug': self.slug})
    # def category_name(self):
    #     all = []
    #     for a in self.category.all():
    #         all.append(str(a))
    #     return "; ".join(all)

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
