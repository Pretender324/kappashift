from django.db import models

# Create your models here.


class CompetitionModel(models.Model):
    name = models.CharField(max_length=50)
    year = models.IntegerField()
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(auto_now=False, auto_now_add=False)
    days = models.IntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=('name', 'year'), name='unique_competition'
            )
        ]
