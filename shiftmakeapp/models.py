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

    def __str__(self):
        return str(self.year) + self.name


class EventModel(models.Model):
    sex = models.CharField(max_length=50, choices=(('M', 'M'), ('W', 'W')))
    distance = models.IntegerField()
    style = models.CharField(max_length=10, choices=(('Fr', 'Fr'), ('Ba', 'Ba'), (
        'Br', 'Br'), ('Fly', 'Fly'), ('IM', 'IM'), ('FR', 'FR'), ('MR', 'MR')))

    def __str__(self):
        return self.sex + str(self.distance) + 'm' + self.style


class ShiftModel(models.Model):
    competition = models.ForeignKey(
        'CompetitionModel', on_delete=models.CASCADE)
    event = models.ForeignKey('EventModel', on_delete=models.CASCADE)
    start_time = models.TimeField(auto_now=False, auto_now_add=False)
    member_count = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.competition) + str(self.event)
