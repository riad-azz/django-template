from django.views import generic
from django.urls import reverse_lazy
from core.forms.contact import ContactForm
from core.models.contact import Contact


class ContactView(generic.FormView):
    template_name = 'core/contact/contact_form.html'
    form_class = ContactForm
    success_url = reverse_lazy("core:contact_success")

    def form_valid(self, form):
        # Process the form data here (e.g., send an email)
        # You can access the form data using form.cleaned_data
        form.save()
        # After processing the form, you can return super().form_valid(form)
        # to perform the default behavior (e.g., redirect to success_url)
        return super().form_valid(form)


class ContactListView(generic.ListView):
    model = Contact
    context_object_name = "messages"
    template_name = 'core/contact/contact_list.html'


class ContactSentView(generic.TemplateView):
    template_name = 'core/contact/contact_success.html'
