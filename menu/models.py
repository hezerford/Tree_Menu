from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    title = models.CharField(max_length=50)
    url = models.CharField(max_length=200, blank=True)
    named_url = models.CharField(max_length=50, blank=True)
    parent = models.ForeignKey(Menu, on_delete=models.CASCADE)

    def __str__(self):
        return self.title