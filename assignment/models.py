from django.db import models

# Create your models here.
class Assignment(models.Model):
    title = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='assigment/pdfs/')

    def __str__(self):
        return self.title