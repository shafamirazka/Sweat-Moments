from django.db import models

# Create your models here.
class MoodEntry(models.Model):
    mood = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    # time = models.DateField(auto_now_add=True)
    description = models.TextField()
    price = models.IntegerField()
    mood_intensity = models.IntegerField()

    @property
    def is_mood_strong(self):
        return self.mood_intensity > 5