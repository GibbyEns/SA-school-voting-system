from django.contrib import admin
from .models import Poll, Choice

# Allows you to edit Choices inline when editing a Poll
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3  # show 3 empty choice fields by default

# Customize the admin view for Poll
class PollAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')  # columns to show in the Poll list view
    inlines = [ChoiceInline]  # include the ChoiceInline here

# Register the Poll model with the custom admin
admin.site.register(Poll, PollAdmin)
