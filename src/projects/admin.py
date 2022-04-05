from django.contrib import admin

# Register your models here.
from .models import Project

# by registering models they are accessible from the admin menu
admin.site.register(Project)