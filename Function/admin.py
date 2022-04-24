from django.contrib import admin

# Register your models here.

from .models import MedlMember, MedlTag, MedlPicture

admin.site.register(MedlMember)

admin.site.register(MedlPicture)

admin.site.register(MedlTag)