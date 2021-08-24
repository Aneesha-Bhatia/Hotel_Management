from django.contrib import admin
from .models import Customer, Customer

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'age','email', 'contactno','coming_from','going_to','photo')
    list_filter = ('id',) 


admin.site.register(Customer, CustomerAdmin)
