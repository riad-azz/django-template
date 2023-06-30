from django.views import generic
from django.urls import reverse_lazy
from core.forms.contact import ContactForm


class ContactView(generic.FormView):
    template_name = 'core/contact/index.html'
    form_class = ContactForm
    success_url = reverse_lazy("core:contact_success")

    def form_valid(self, form):
        # Process the form data here (e.g., send an email)
        # You can access the form data using form.cleaned_data
        form.save()
        # After processing the form, you can return super().form_valid(form)
        # to perform the default behavior (e.g., redirect to success_url)
        return super().form_valid(form)


class ContactSentView(generic.TemplateView):
    template_name = 'core/contact/contact_success.html'
