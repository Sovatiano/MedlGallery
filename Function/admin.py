from django.contrib import admin

# Register your models here.

from .models import MedlTag, MedlPicture


admin.site.register(MedlPicture)

admin.site.register(MedlTag)