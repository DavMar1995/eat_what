from django.contrib import admin
from  .models  import *

# Register your models here.

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['name']
    # list_editable = ['name']
    pass
    
admin.site.register(Restaurant, RestaurantAdmin)