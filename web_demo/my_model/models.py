from django.db import models

# Create your models here.


class Test(models.Model):
    email = models.EmailField(verbose_name='email')

    class Meta:
        verbose_name = 'Test'
        verbose_name_plural = verbose_name