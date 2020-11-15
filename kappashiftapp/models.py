from django.db import models

# Create your models here.


class MemberModel(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    grade = models.IntegerField()
    sex = models.CharField(max_length=50, choices=(('男', 'M'), ('女', 'W')))
    member_type = models.CharField(max_length=10, choices=(
        ('選手', 'Swimmer'), ('マネージャー', 'Manager')))

    def __str__(self):
        return self.last_name + self.first_name
