from django import forms
from django.core.validators import FileExtensionValidator

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        print(f'Sending email from {self.cleaned_data["email"]} with message: {self.cleaned_data["message"]}')