# Generated by Django 3.1 on 2020-09-06 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shiftmakeapp', '0002_auto_20200906_1250'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShiftModel',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField()),
                ('member_count', models.IntegerField()),
                ('competition', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='shiftmakeapp.competitionmodel')),
                ('event', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='shiftmakeapp.eventmodel')),
            ],
        ),
    ]
