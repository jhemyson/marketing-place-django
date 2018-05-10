from django.conf.urls import url, include
from django.contrib import admin
from ajax_select import  urls as ajax_select_urls


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^ajax_select/', include(ajax_select_urls)),
]
