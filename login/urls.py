from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^register', views.register, name='login_register'),
    url(r'^register/success', views.register_success, name='login_register_success'),
]