from django.contrib import admin

from .models import Flat, Claim, Owner


class FlatAdmin(admin.ModelAdmin):
    raw_id_fields = ("liked_by", "owners")
    search_fields = ("town", "address", "owners__name", "owners__pure_phone")
    readonly_fields = ("created_at",)
    list_display = (
        "address",
        "price",
        "new_building",
        "construction_year",
        "town",
        "get_owners",
    )
    list_editable = ("new_building",)
    list_filter = ("new_building", "rooms_number", "has_balcony", "active")


class ClaimAdmin(admin.ModelAdmin):
    raw_id_fields = ("author", "flat")
    search_fields = ("flat__address", "text", "author__last_name", "author__first_name")
    list_display = ("flat", "text", "author")
    list_filter = ("author",)


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ("flats",)
    search_fields = ("name", "pure_phone")
    list_display = ("name", "pure_phone")


admin.site.register(Flat, FlatAdmin)
admin.site.register(Claim, ClaimAdmin)
admin.site.register(Owner, OwnerAdmin)
