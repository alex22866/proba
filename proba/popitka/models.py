from django.db import models


class Header(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name



class Headerdis(models.Model):
    header = models.ForeignKey(Header, on_delete=models.CASCADE)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return self.last_name