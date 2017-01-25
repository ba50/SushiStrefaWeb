"""
Definition of urls for DjangoWebSushiStrefa.
"""

from django.conf.urls import url
from app import views
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [

    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/images/SUSHI_STREFA_LOGO_Web.jpg')),
    url(r'^$', views.home, name='home'),
    url(r'^menu$', views.menu, name='menu'), 
    url(r'^delivery_zone$', views.dev_zone, name='delivery_zone'),
    url(r'^gallery$', views.gallery, name='gallery'),
    url(r'^about$', views.about, name='about'),
    url(r'^contact$', views.contact, name='contact'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
