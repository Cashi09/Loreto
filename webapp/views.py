from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import *
from .models import *

# Create your views here.


def home(request):
    contactUsForm = ContactUsForm
    context = {
        'contactForm' : contactUsForm
    }
    if request.method == 'POST':
        contactUsForm = contactUsForm(request.POST)
        if contactUsForm.is_valid():
            contactUsForm.save()
            messages.add_message(request, messages.INFO, 'Message Sent!')
            return redirect(to="home")
        context = {
            'contactForm' : contactUsForm
        }
        return render(request, 'pages/home.html', context)
    
    
    return render(request, "pages/home.html", context)


def sign_in(request):
    if request.user.is_authenticated:
        return redirect(to="home")
    if request.method == "POST":
        credential = {
            "username": request.POST.get("username"),
            "password": request.POST.get("password"),
        }
        authenticate_user = authenticate(
            username=credential["username"], password=credential["password"]
        )

        if authenticate_user is not None:
            login(request, authenticate_user)

            return redirect(to="home")

        return render(request, "pages/login.html")

    return render(request, "pages/login.html")


def sign_up(request):
    return render(request, "pages/register.html")


def about(request):
    return render(request, "pages/about.html")


def product_page(request):
    orders = CustomizedBoxOrder.objects.all()
    orderForm = CustomizedBoxOrderForm
    clientForm = ClientForm
    context = {"orderForm": orderForm, "clientForm": clientForm, "orders": orders}
    if request.method == "POST":
        orderForm = CustomizedBoxOrderForm(request.POST)
        if orderForm.is_valid():
            orderForm.save()
            return redirect(to="product")

        context = {"orderForm": orderForm, "clientForm": clientForm, "orders": orders}
        return render(request, "pages/product.html", context)

    return render(request, "pages/product.html", context)


def user_profile(request):
    return render(request, "pages/userprofile.html")


def save_client(request):
    clientForm = ClientForm(request.POST)
    if clientForm.is_valid():
        clientForm.save()
        return redirect(to="product")
    return redirect(to="product")


@login_required(login_url="login")
def dashboard(request):
    totalOrders = CustomizedBoxOrder.objects.count()
    orders = CustomizedBoxOrder.objects.all()
    totalInquiries = ContactUs.objects.count()
    context = {
        "orderTotals": totalOrders, 
        "orders": orders,
        "totalInquiries" : totalInquiries
        }

    return render(request, "pages/dashboard/index.html", context)


@login_required(login_url="login")
def contact_index(request):
    contacts = ContactUs.objects.all()
    context = {
        'contacts' : contacts
    }
    return render(request, 'pages/dashboard/contacts/index.html', context)


@login_required(login_url="login")
def contact_show(request, contactID):
    contact = ContactUs.objects.filter(id=contactID).first()
    context = {
        'contact' : contact
    }
    
    return render(request, 'pages/dashboard/contacts/show.html', context)


@login_required(login_url="login")
def contact_edit(request, contactID):
    contact = ContactUs.objects.filter(id=contactID).first()
    context = {
        'contact' : contact
    }
    if request.method == 'POST':
        contactData = {
            'name' : request.POST.get('contact_name'),
            'email' : request.POST.get('contact_email'),
            'message' : request.POST.get('contact_message')
        }
        contact.name = contactData['name']
        contact.email = contactData['email']
        contact.message = contactData['message']
        contact.save()
        messages.add_message(request, messages.INFO, 'Contact Details Updated')
        return redirect(to="contact_index")
    
    return render(request, 'pages/dashboard/contacts/edit.html', context)




@login_required(login_url="login")
def contact_delete(request, contactID):
    contact = ContactUs.objects.filter(id=contactID).first()
    contact.delete()
    return redirect(to='contact_index')


@login_required(login_url="login")
def order_index(request):
    orders = CustomizedBoxOrder.objects.all()
    context = {
        'orders' : orders
    }
    
    return render(request, 'pages/dashboard/orders/index.html', context)

@login_required(login_url="login")
def  order_delete(request, orderID):
    order = CustomizedBoxOrder.objects.filter(id=orderID).first()
    order.delete()
    return redirect(to="order_index")


@login_required(login_url='login')
def order_show(request, orderID):
    order = CustomizedBoxOrder.objects.filter(id=orderID).first()
    context = {
        'order' : order
    }
    return render(request, 'pages/dashboard/orders/show.html', context)

@login_required(login_url='login')
def order_edit(request, orderID):
    order = CustomizedBoxOrder.objects.filter(id=orderID).first()
    context = {
        'order' : order,
        'orderForm' : CustomizedBoxOrderForm
    }
    
    if request.method == 'POST':
        orderForm = CustomizedBoxOrderForm(request.POST, instance=order)
        orderForm.save()
        messages.add_message(request, messages.INFO, 'Data Detailed Updated')
        return redirect(to="order_index")
    
    return render(request, 'pages/dashboard/orders/edit.html', context)
    

@login_required(login_url="login")
def sign_out(request):
    logout(request)
    return render(request, "pages/home.html")
