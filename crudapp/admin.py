from django.contrib import admin

from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("oid", "fname", "lname", "price", "mail")
    search_fields = ("oid", "fname", "lname", "mail")
    list_filter = ("lname",)
