from django.contrib import admin
from django.urls import path

from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('contacts/', views.contacts, name='contact'),
]

# Django admin customisation

admin.site.site_header = 'Portfolio'
admin.site.index_title = 'welcome to this Portfolio site'
admin.site.site_title = 'Portfolio'
