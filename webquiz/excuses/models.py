from django.db import models


class Sentence(models.Model):
    def __str__(self):
        return self.content_text
    content_text = models.CharField(max_length=200)
