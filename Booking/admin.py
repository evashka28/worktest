from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from Booking.models import CustomUser, Room, Reservation

admin.site.register(CustomUser, UserAdmin)
admin.site.register(Room)
admin.site.register(Reservation)
