from django.db import models

class MenuItem(models.Model):
    title = models.CharField(max_length=50)
    url = models.URLField()
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title