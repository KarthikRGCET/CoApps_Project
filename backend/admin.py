from django.contrib import admin

from backend.models import Country, State, City, Company_details, Job_category, Job_apply


# Register your models here.
@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    pass

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass

@admin.register(Job_category)
class Job_categoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Job_apply)
class Job_applyAdmin(admin.ModelAdmin):
    pass


@admin.register(Company_details)
class CompanyDetailsAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'email_address', 'posted_date', 'job_nature']
    list_filter = ['job_nature', 'posted_date']
    search_fields = ['company_name', 'email_address']
    date_hierarchy = 'posted_date'

