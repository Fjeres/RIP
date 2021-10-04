from django.db import models


class Todolist(models.Model):
    name = models.CharField(max_length=100)
    checked = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('id',)
