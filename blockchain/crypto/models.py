from django.db import models


class Crypto(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='crypto/images/')
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
