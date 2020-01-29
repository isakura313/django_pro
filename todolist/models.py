from django.db import models

# Create your models here.
from django.utils import timezone
# в наших делах можно будет посмотреть время


class Category(models.Model): #таблица категорий имя которая наследует models.Model
    name = models.CharField(max_length = 100)  #создаем первую категорию varchar

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")
    def __str__(self):
        return self.name #имя которое показывается когда она вызывается

class TodoList(models.Model):
    title = models.CharField(max_length=250) #таблица
    content = models.TextField(blank=True)  # сам контент нашей todo
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))  # a date
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))  # a date
    category = models.ForeignKey(Category, default="general", on_delete=models.PROTECT)  # a foreignkey

    class Meta:
        ordering = ["-created"]  # ordering by the created field

    def __str__(self):
        return self.title  # name to be shown when called




