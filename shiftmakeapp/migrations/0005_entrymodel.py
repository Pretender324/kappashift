# Generated by Django 3.1 on 2020-10-12 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kappashiftapp', '0002_auto_20200830_0926'),
        ('shiftmakeapp', '0004_auto_20200921_1351'),
    ]

    operations = [
        migrations.CreateModel(
            name='EntryModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kappashiftapp.membermodel')),
                ('shift', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shiftmakeapp.shiftmodel')),
            ],
        ),
    ]
