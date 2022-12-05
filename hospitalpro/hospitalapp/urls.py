from django.urls import path,include
from .import views
urlpatterns = [
    path('',views.index,name='home'),
    path('about',views.about,name='about'),
    path('booking',views.booking,name='book'),
    path('contact',views.contact,name='contact'),
    path('department',views.department,name='dept'),
    path('doctor',views.doctor,name='doct')
]
