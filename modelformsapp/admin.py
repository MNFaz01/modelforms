from django.contrib import admin
from modelformsapp.models import Projects

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display=['id','startDate','endDate','name','assignedTo','priority']

admin.site.register(Projects,ProjectAdmin)
