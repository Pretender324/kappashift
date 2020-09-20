from django.contrib import admin
from .models import CompetitionModel, EventModel, ShiftModel

# Register your models here.
admin.site.register(CompetitionModel)
admin.site.register(EventModel)
admin.site.register(ShiftModel)
