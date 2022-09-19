from django.contrib import admin
from .models import PortfolioItem, TeamMember

# Register your models here.
class PortfolioItemAdmin(admin.ModelAdmin):
    list_display = ['heading','completed_on']
    readonly_fields = ['completed_on']
    ordering = ('-completed_on',)

class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'joined_on']
    readonly_fields = ['joined_on']
    ordering = ('-joined_on',)

admin.site.register(PortfolioItem, PortfolioItemAdmin)
admin.site.register(TeamMember, TeamMemberAdmin)