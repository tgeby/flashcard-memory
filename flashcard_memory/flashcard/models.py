from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Flashcard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    term = models.CharField(max_length=255)
    definition = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.term
    
class Deck(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    flashcards = models.ManyToManyField(Flashcard, related_name="decks")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name