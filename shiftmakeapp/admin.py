from django.contrib import admin
from .models import CompetitionModel, EventModel, ShiftModel, EntryModel

# Register your models here.
admin.site.register(CompetitionModel)
admin.site.register(EventModel)
admin.site.register(ShiftModel)
admin.site.register(EntryModel)
