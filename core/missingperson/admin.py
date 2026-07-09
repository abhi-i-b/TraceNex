from django.contrib import admin

from .models import (
    MissingPerson,
    DetectionLog,
    Police
)


# Register Models

admin.site.register(MissingPerson)
admin.site.register(DetectionLog)
admin.site.register(Police)