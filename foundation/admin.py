from django.contrib import admin
from .models import Activity, Volunteer, Donation
@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ('donor_name', 'amount', 'purpose', 'date', 'status')

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'hours')

admin.site.register(Volunteer)
# Register your models here.
