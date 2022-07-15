from django.contrib import admin
from  .models  import *

# Register your models here.

class RestaurantAdmin(admin.ModelAdmin):
    # list_display = ['id','title']
    # list_editable = ['title']
    pass
    
admin.site.register(Restaurant, RestaurantAdmin)