from django.db import models
from kappashiftapp.models import MemberModel

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
        'CompetitionModel', on_delete=models.CASCADE, related_name='shift')
    event = models.ForeignKey('EventModel', on_delete=models.CASCADE)
    start_time = models.TimeField(auto_now=False, auto_now_add=False)
    video = models.ForeignKey(
        MemberModel, on_delete=models.CASCADE, related_name='video_shift', null=True, blank=True)
    timekeep = models.ForeignKey(
        MemberModel, on_delete=models.CASCADE, related_name='timekeep_shift', null=True, blank=True)

    def __str__(self):
        return str(self.competition) + str(self.event)

    def member_count(self):
        return self.entry.count()


class EntryModel(models.Model):
    member = models.ForeignKey(MemberModel, on_delete=models.CASCADE)
    shift = models.ForeignKey(
        'ShiftModel', on_delete=models.CASCADE, related_name='entry')

    def __str__(self):
        return str(self.shift) + str(self.member)
