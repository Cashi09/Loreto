# admin.py

from django.contrib import admin
from .models import Employee, Client, CustomizedBoxOrder, Registration, ContactUs

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'position', 'department')
    search_fields = ('username', 'first_name', 'last_name', 'email', 'position', 'department')

class ClientAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'contact_person', 'contact_number', 'email')
    search_fields = ('company_name', 'contact_person', 'contact_number', 'email')

class CustomizedBoxOrderAdmin(admin.ModelAdmin):
    list_display = ('po_number', 'jdy_code_number', 'fty_item_number', 'item_description',
                    'qty_per_carton', 'total_carton_order', 'size_length', 'size_width',
                    'size_height', 'size_unit', 'weight', 'client', 'order_date', 'delivery_date')
    search_fields = ('po_number', 'jdy_code_number', 'fty_item_number', 'item_description')

class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('username', 'client_type')  # Adjust list_display accordingly
    search_fields = ('username', 'client_type')

class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')
    search_fields = ('name', 'email', 'message')

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(CustomizedBoxOrder, CustomizedBoxOrderAdmin)
admin.site.register(Registration, RegistrationAdmin)
admin.site.register(ContactUs, ContactUsAdmin)