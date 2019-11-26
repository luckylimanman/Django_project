from django.db import models


class Restaurant(models.Model):
    restuarant_text = models.CharField(max_length=200)
    restuarant_evaluate = models.IntegerField()

    def __str__(self):
        return self.restuarant_text
