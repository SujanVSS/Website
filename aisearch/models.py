from django.db import models

class Search(models.Model):
    text = models.CharField(max_length = 150, blank = False, null = False)

    def __str__(self):
        return self.text