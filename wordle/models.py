from django.db import models
from django.conf import settings

USER_MODEL = settings.AUTH_USER_MODEL


class WordleHistory(models.Model):
    player = models.ForeignKey(
        USER_MODEL,
        related_name="wordlehistory",
        on_delete=models.CASCADE,
        null = True
    )
    word = models.CharField(max_length=10)
    length = models.IntegerField(default=5, verbose_name="Word length")
    duplicates = models.BooleanField(default=False, verbose_name="Allow duplicate letters")
    tries = models.IntegerField(default=6, verbose_name="Guesses allowed")
    guesses_needed = models.IntegerField(null=True,blank=True)
    cleared = models.BooleanField(default=False)
    attempted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id} {self.word}'
