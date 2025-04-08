from django.contrib import admin
from .models import Utilisateur, Livre, Emprunt, Reservation, Notification
from django.contrib.auth.admin import UserAdmin

admin.site.register(Utilisateur, UserAdmin)
admin.site.register(Livre)
admin.site.register(Emprunt)
admin.site.register(Reservation)
admin.site.register(Notification)
