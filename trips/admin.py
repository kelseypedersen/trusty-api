from django.contrib import admin

from .models import User, Overview, Segment

admin.site.register(Overview)
admin.site.register(Segment)
admin.site.register(User)

# Register your models here.
