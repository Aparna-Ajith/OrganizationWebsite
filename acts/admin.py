from django.contrib import admin
from acts.models import Acts

# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    pass


admin.site.register(Acts, ProjectAdmin)
