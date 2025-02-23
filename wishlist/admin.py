from django.contrib import admin
from .models import Wishlist, WishlistItem

class WishlistItemInline(admin.TabularInline):
    model = WishlistItem
    extra = 0
    readonly_fields = ('date_added',)
    can_delete = True

class WishlistAdmin(admin.ModelAdmin):
    list_display = ('user',)
    inlines = [
        WishlistItemInline,
    ]

admin.site.register(Wishlist, WishlistAdmin)