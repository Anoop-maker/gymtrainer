from django.contrib import admin

from courses.models import Trainer, Class

# Register your models here.
admin.site.register(Trainer)
admin.site.register(Class)