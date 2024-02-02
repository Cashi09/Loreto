from django import forms
from .models import  *





class CustomizedBoxOrderForm(forms.ModelForm):
    class Meta:
        model = CustomizedBoxOrder
        fields = '__all__'
        widgets = {
            'po_number': forms.TextInput(attrs={'class': 'block mb-2 text-sm font-medium text-gray-900 p-2', 'placeholder': 'po_number'}),
            'jdy_code_number': forms.TextInput(attrs={'class': 'block mb-2 text-sm font-medium text-gray-900 p-2', 'placeholder': 'jdy_code_number'}),
            'fty_item_number': forms.TextInput(attrs={'class': 'block mb-2 text-sm font-medium text-gray-900 p-2', 'placeholder': 'fty_item_number'}),
            'item_description': forms.Textarea(attrs={'class': 'block mb-2 text-sm font-medium text-gray-900 p-2', 'placeholder': 'item_description'}),
            'qty_per_carton': forms.NumberInput(attrs={'class': 'block mb-2 text-sm font-medium text-gray-900 p-2', 'placeholder': 'qty_per_carton'}),
            'total_carton_order': forms.NumberInput(attrs={'class': 'block mb-2 text-sm font-medium text-gray-900 p-2', 'placeholder': 'total_carton_order'}),
            'size_length': forms.NumberInput(attrs={'class': 'block mb-2 text-sm font-medium text-gray-900 p-2',  'placeholder': 'size_length'}),
            'size_width': forms.NumberInput(attrs={'class': 'block mb-2 text-sm font-medium text-gray-900 p-2', 'placeholder': 'size_width'}),
            'size_height': forms.NumberInput(attrs={'class': 'block mb-2 text-sm font-medium text-gray-900 p-2', 'placeholder': 'size_height'}),
            'size_unit': forms.Select(attrs={'class': 'block mb-2 text-sm font-medium text-gray-900 p-2', 'placeholder': 'size_unit'}),
            'weight': forms.NumberInput(attrs={'class': 'block mb-2 text-sm font-medium text-gray-900 p-2', 'placeholder': 'weight' }),
            'client': forms.Select(attrs={'class': 'block mb-2 text-sm font-medium text-gray-900 p-2', 'placeholder': 'client' }),
            'order_date': forms.DateInput(attrs={'class': 'block mb-2 text-sm font-medium text-gray-900 p-2', 'type': 'date', 'placeholder': 'order_date' }),
            'delivery_date': forms.DateInput(attrs={'class': 'block mb-2 text-sm font-medium text-gray-900 p-2', 'type': 'date', 'placeholder': 'delivery_date' }),
        }
        
class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        widgets = {
            'company_name' : forms.TextInput(attrs={'class' : 'block mb-2 text-sm font-medium text-gray-900 p-2', 'placeholder': 'Company Name'}),
            'contact_person' : forms.TextInput(attrs={'class' : 'block mb-2 text-sm font-medium text-gray-900 p-2', 'placeholder': 'Company Person'}),
            'contact_number' : forms.TextInput(attrs={'class' : 'block mb-2 text-sm font-medium text-gray-900 p-2', 'placeholder': 'Company Number'}),
            'email' :  forms.TextInput(attrs={'class' : 'block mb-2 text-sm font-medium text-gray-900 p-2', 'placeholder': 'Company Number', 'type': 'email'}),
        }
        
class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = '__all__'
        widgets = {
            'name'  : forms.TextInput(attrs={'class' : 'block mb-2 text-sm font-medium text-gray-900 p-2', 'placeholder': 'Name'}),
            'email'  : forms.EmailInput(attrs={'class' : 'block mb-2 text-sm font-medium text-gray-900 p-2', 'placeholder': 'Email'}),
            'message'  : forms.Textarea(attrs={'class' : 'block mb-2 text-sm font-medium text-gray-900 p-2', 'placeholder': 'Message'}),
        }