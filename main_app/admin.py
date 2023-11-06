from django.contrib import admin
from .models import User, Stats
from .models import Drill_data
# Register your models here.
admin.site.register(User)
admin.site.register(Stats)
admin.site.register(Drill_data)
