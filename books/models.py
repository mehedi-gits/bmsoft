from django.db import models

# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=100, verbose_name="Book Title")
    author = models.CharField(max_length=100, verbose_name="Author")
    description = models.TextField(verbose_name="Book Description")
    pub_year = models.PositiveBigIntegerField(verbose_name="Publication Year")

    def __str__(self):
        return self.title