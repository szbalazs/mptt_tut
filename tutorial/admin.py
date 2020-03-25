from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from tutorial.models import Genre

# Register your models here.
admin.site.register(
    Genre,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
    ),
    list_display_links = (
        'indented_title',
    ),
)
