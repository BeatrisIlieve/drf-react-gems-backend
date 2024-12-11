from django.db import models

from drf_react_gems_backend.product.managers import ProductManager


class Category(models.Model):
    TITLE_CHOICES = (
        ("E", "Earrings"),
        ("B", "Bracelets"),
        ("N", "Necklaces"),
        ("R", "Rings"),
        ("C", "Charms"),
        ("P", "Pendants"),
    )

    title = models.CharField(
        max_length=1,
        choices=TITLE_CHOICES,
    )

    def __str__(self):
        return self.get_title_display()


class Color(models.Model):
    TITLE_CHOICES = (
        ("P", "Pink"),
        ("B", "Blue"),
        ("W", "White"),
    )

    title = models.CharField(
        max_length=1,
        choices=TITLE_CHOICES,
    )

    def __str__(self):
        return self.get_title_display()


class Product(models.Model):

    objects = ProductManager()

    first_image_url = models.URLField()

    second_image_url = models.URLField()

    category = models.ForeignKey(
        to=Category,
        on_delete=models.CASCADE,
    )

    color = models.ForeignKey(
        to=Color,
        on_delete=models.CASCADE,
    )

    description = models.TextField(
        max_length=300,
    )

    def __str__(self):
        return f"{self.color.get_title_display()} {self.category.get_title_display()}"
