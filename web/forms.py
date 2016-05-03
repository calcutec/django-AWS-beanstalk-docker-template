from django import forms
from django.core.mail import mail_managers

class ContactForm(forms.Form):
    contact_name = forms.CharField(label='Your Name', max_length=40, required=True)
    contact_email = forms.EmailField(label='Your E-Mail Address', required=True)
    contact_phone = forms.CharField(label='Telephone', max_length=20)
    content = forms.CharField(label='Message', widget=forms.Textarea, required=True)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = "Your name:"
        self.fields['contact_email'].label = "Your email:"
        self.fields['contact_phone'].label = "Your telephone:"
        self.fields['content'].label = "What is your message?"

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass
