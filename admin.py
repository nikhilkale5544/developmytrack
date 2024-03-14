from django.contrib import admin
from .models import Travel

# @admin.register(Pet)
class TravelAdmin(admin.ModelAdmin):
     list_display=('id','Yourname','Destination','Person','HowmanyDays')

# Register your models here.

admin.site.register(Travel, TravelAdmin)
