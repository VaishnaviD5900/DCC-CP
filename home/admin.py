from django.contrib import admin

# Register your models here.
from django.contrib import admin
from home.models import Booking
from home.models import Users



admin.site.register(Booking)
admin.site.register(Users)
