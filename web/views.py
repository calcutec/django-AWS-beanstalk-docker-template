from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import EmailMessage, BadHeaderError
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from django.utils.timezone import now
from django.views.generic import TemplateView, FormView
from web.forms import ContactForm

class IndexView(TemplateView):
    template_name = "index.html"

class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        if now().weekday() < 5 and 8 < now().hour < 22:
            context['open'] = True
        else:
            context['open'] = False
        return context

class ContactView(SuccessMessageMixin, FormView):
    form_class = ContactForm
    success_url = reverse_lazy('contact')
    success_message = "Your message was sent successfully. We will respond to you soon. Thank you!"
    template_name = 'contact.html'

    def form_valid(self, form):
        contact_name = form.cleaned_data['contact_name']
        contact_email = form.cleaned_data['contact_email']
        contact_phone = form.cleaned_data['contact_phone']
        form_content = form.cleaned_data['content']
        to_recipient  = ['Kevin Coyner <kevin@rustybear.com>']
        bcc = ['kevin@rustybear.com']
        from_email = 'Postmaster <postmaster@rustybear.com>'
        subject = '[Rustybear] Website Contact'
        ip_address = self.request.META['REMOTE_ADDR']

        template = get_template('contact_template.txt')
        context = {
            'contact_name': contact_name,
            'contact_email': contact_email,
            'contact_phone': contact_phone,
            'form_content': form_content,
            'ip_address': ip_address
        }
        content = template.render(context)

        email = EmailMessage(
            subject,
            content,
            from_email,
            to_recipient,
            bcc,
            reply_to=[contact_name + ' <' +contact_email + '>'],
        )
        email.send()
        return super(ContactView, self).form_valid(form)

