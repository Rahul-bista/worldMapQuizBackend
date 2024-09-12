from django.db import models

# Create your models here.
class GuessTheFlag(models.Model):
    flag_image = models.ImageField(upload_to='flags/')
    option1 = models.CharField(max_length=50)
    option2 = models.CharField(max_length=50)
    option3 = models.CharField(max_length=50)
    correct_answer = models.CharField(max_length=50)

    def __str__(self):
        return f"Flag Question: {self.correct_answer}"
