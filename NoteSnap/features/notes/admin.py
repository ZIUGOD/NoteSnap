from django.contrib import admin
from .models import Note

@admin.register(Note)
class NotesAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at', 'is_private')
    list_filter = ('author', 'is_private')
    search_fields = ('title', 'text', 'author')
    # readonly_fields = ('created_at', 'updated_at')