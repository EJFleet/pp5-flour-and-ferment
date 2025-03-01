from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'subject',
        'status',
        'created_at',
    )

    list_filter = (
        'status',
        'created_at',
    )

    search_fields = (
        'name',
        'email',
        'subject',
        'message',
    )

    actions = [
        'mark_as_read',
        'mark_as_unread',
    ]

    date_hierarchy = 'created_at'

    def mark_as_read(self, request, queryset):
        queryset.update(status='read')
        self.message_user(
            request, f"{queryset.count()} message(s) marked as read."
        )
    mark_as_read.short_description = "Mark selected messages as read"

    def mark_as_unread(self, request, queryset):
        queryset.update(status='unread')
        self.message_user(
            request, f"{queryset.count()} message(s) marked as unread."
        )
    mark_as_unread.short_description = "Mark selected messages as unread"


admin.site.register(Contact, ContactAdmin)
