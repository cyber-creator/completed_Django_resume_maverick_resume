from django.forms import ModelForm
from .models import ContactFrom


class ContactForm(ModelForm):
    class Meta:
        model = ContactFrom
        fields = ['name', 'phone']

