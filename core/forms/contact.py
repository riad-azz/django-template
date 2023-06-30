from django import forms
from django.core.exceptions import ValidationError

from core.models.contact import Contact
from django.core.validators import EmailValidator, MinValueValidator


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'title', 'message')

    def clean_name(self):
        name = self.cleaned_data.get('name')
        min_validator = MinValueValidator(limit_value=2)
        try:
            min_validator(len(name))
        except ValidationError as e:
            raise forms.ValidationError("Name can't be shorter than 2 characters")

        return name

    def clean_title(self):
        title = self.cleaned_data.get('title')
        min_validator = MinValueValidator(limit_value=10)
        try:
            min_validator(len(title))
        except ValidationError as e:
            raise forms.ValidationError("Title can't be shorter than 10 characters")

        return title

    def clean_message(self):
        message = self.cleaned_data.get('message')
        min_validator = MinValueValidator(limit_value=50)
        try:
            min_validator(len(message))
        except ValidationError as e:
            raise forms.ValidationError("Message can't be shorter than 50 characters")

        return message

    def clean_email(self):
        email = self.cleaned_data.get('email')

        email_validator = EmailValidator()
        try:
            email_validator(email)
        except ValidationError as e:
            raise forms.ValidationError(str(e))

        return email
