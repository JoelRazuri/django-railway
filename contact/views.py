from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .models import Contact
from .forms import ContactForm



class ContactListView(ListView):
    model = Contact
    template_name = 'contact/index.html'
    context_object_name = 'contacts'



class ContactDetailView(DetailView):
    model = Contact
    template_name = 'contact/detail.html'
    context_object_name = 'contact'



class ContactCreateView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contact/create.html'
    success_url = reverse_lazy('contact')



class ContactUpdateView(UpdateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contact/update.html'
    success_url = reverse_lazy('contact')
    context_object_name = 'contact'



def delete(request, id):
    contact = Contact.objects.get(id=id)
    contact.delete()

    return redirect('contact')

