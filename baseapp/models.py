from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    cat_name = models.CharField(verbose_name="Category", max_length=155)

    def __str__(self):
        return self.cat_name

    class Meta:
        verbose_name_plural = "Categories"
        verbose_name = "Category"
        ordering = ['cat_name']


class RoomModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name="User")
    title = models.CharField(verbose_name="Title", max_length=200)
    content = models.TextField(verbose_name="Content")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, blank=True, verbose_name="Category",)
    created = models.DateTimeField(verbose_name="Created", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Updated", auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created", '-updated']


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')
    room = models.ForeignKey(RoomModel, on_delete=models.CASCADE, null=True, blank=True)
    message = models.TextField(verbose_name="Message")
    created = models.DateTimeField(verbose_name="Created", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Updated", auto_now=True)

    def __str__(self):
        return self.message[:40]
