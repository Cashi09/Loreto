# Loreto, Kyla Cashmire P. - BSIT 3-1
# models.py

from django.contrib.auth.models import BaseUserManager, AbstractUser
from django.db import models

class EmployeeManager(BaseUserManager):
    def create_employee(self, *args, **kwargs):
        # Custom logic for creating an employee
        # e.g., assigning default groups, permissions, etc.
        return super().create(*args, **kwargs)

class Employee(AbstractUser):
    """
    Custom User model for representing employees.
    """
    objects = EmployeeManager()

    position = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    consent_to_save = models.BooleanField(default=False)

    def __str__(self):
        """
        Return a human-readable representation of the employee.
        """
        return f"{self.first_name} {self.last_name} ({self.username}) - {self.position} in {self.department}"

class Client(models.Model):
    company_name = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=11)
    email = models.EmailField()
    consent_to_save = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.company_name} - {self.contact_person}"

class CustomizedBoxOrder(models.Model):
    SIZE_UNIT_CHOICES = [
        ('inches', 'Inches'),
        ('cm', 'Centimeters'),
    ]

    po_number = models.CharField(max_length=20, unique=True)
    jdy_code_number = models.CharField(max_length=20, unique=True)
    fty_item_number = models.CharField(max_length=20, unique=True)
    item_description = models.TextField()
    qty_per_carton = models.PositiveIntegerField()
    total_carton_order = models.PositiveIntegerField()
    size_length = models.FloatField()
    size_width = models.FloatField()
    size_height = models.FloatField()
    size_unit = models.CharField(max_length=10, choices=SIZE_UNIT_CHOICES)
    weight = models.FloatField()

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    order_date = models.DateField(auto_now_add=True)
    delivery_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Order {self.po_number} - {self.item_description} for {self.client}"

class Registration(models.Model):
    username = models.CharField(max_length=150, unique=True)
    screen_name = models.CharField(max_length=150, default='')  # Set a default value
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    client_type = models.CharField(max_length=20, choices=[('Individual', 'Individual'), ('Company', 'Company')])
    picture = models.ImageField(upload_to='registration_pictures/', blank=True, null=True)

    def __str__(self):
        return f"Registration - {self.username}"

class ContactUs(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"Contact Us - {self.name}"

# Set unique related_names for groups and user_permissions to avoid clashes
Employee._meta.get_field('groups').remote_field.related_name = 'employee_groups'
Employee._meta.get_field('user_permissions').remote_field.related_name = 'employee_user_permissions'

