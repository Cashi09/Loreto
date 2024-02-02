from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.sign_in, name="login"),
    path('register/', views.sign_up, name="register"),
    path('about/', views.about, name="about"),
    path('product/', views.product_page, name="product"),
    path('client', views.save_client, name="save_client"),
    path('userprofile/', views.user_profile, name="userprofile"),
    path('logout', views.sign_out, name="logout"),
    path('dashboard/', include([
        path('', views.dashboard, name="dashboard"),
        path('contacts/', include([
            path('', views.contact_index, name="contact_index"),
            path('delete/<int:contactID>', views.contact_delete, name="contact_delete"),
            path('show/<int:contactID>', views.contact_show, name="contact_show"),
            path('edit/<int:contactID>', views.contact_edit, name="contact_edit")
        ])),
        path('orders/', include([
            path('', views.order_index, name="order_index"),
            path('delete/<int:orderID>', views.order_delete, name="order_delete"),
            path('show/<int:orderID>', views.order_show, name="order_show"),
            path('edit/<int:orderID>', views.order_edit, name="order_edit")
        ]))
    ]))
]
