from django.db import models


class School(models.Model):
    school_name = models.CharField(max_length=20)
    school_population = models.IntegerField(default=100)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.school_name
