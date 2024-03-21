from django.urls import path
from .views import ContactListView, ContactDetailView, ContactCreateView, ContactUpdateView
from . import views

urlpatterns = [
    path('', ContactListView.as_view(), name='contact'),
    path("create/", ContactCreateView.as_view(), name='contact_create'),
    path('view/<slug:pk>', ContactDetailView.as_view(), name='contact_view'),
    path('uptdate/<slug:pk>', ContactUpdateView.as_view(), name='contact_update'),
    path('delete/<int:id>', views.delete, name='contact_delete'),
]
   
