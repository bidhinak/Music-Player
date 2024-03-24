from django.contrib import admin

from playerapp import models

# Register your models here.
admin.site.register(models.Login)
admin.site.register(models.Artist_Table)
admin.site.register(models.Users)
