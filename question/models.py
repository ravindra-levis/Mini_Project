from django.db import models

# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='question/pdfs/')

    def __str__(self):
        return self.title
