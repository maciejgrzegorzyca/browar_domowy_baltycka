from django.contrib import admin
from .models import Batch

# Register your models here.

class BatchAdmin(admin.ModelAdmin):
    list_display = ('namebatch', 'stylebatch', "ogbatch", "abvbatch", "ibubatch")


admin.site.register(Batch, BatchAdmin)