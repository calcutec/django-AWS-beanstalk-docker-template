from django.test import TestCase
from django.core.urlresolvers import reverse
from django.forms import EmailField, CharField

import datetime
from django.utils import timezone

from nataleconst.forms import ContactForm
from nataleconst.views import ContactView

#class QuestionAboutTests(TestCase):
#    def test_was_published_recently_with_future_question(self):
#        time = timezone.now() + datetime.timedelta(days=30)
#        future_question = Question(pub_date=time)
#        self.assertEqual(future_question.was_published_recently(), False)


class NataleconstViewsTestCase(TestCase):
    def test_index(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
        resp = self.client.get(reverse("home"))
        self.assertEqual(resp.status_code, 200)

    def test_about(self):
        resp = self.client.get('/about/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('open' in resp.context)
        resp = self.client.get(reverse("about"))
        self.assertEqual(resp.status_code, 200)

    def test_contact(self):
        resp = self.client.get('/contact/')
        self.assertEqual(resp.status_code, 200)
        resp = self.client.get(reverse("contact"))
        self.assertEqual(resp.status_code, 200)

    def test_contact_form_is_valid(self):
        form = ContactForm({'contact_name': 'Kevin', 
                     'contact_email': 'kevin@example.com',
                     'contact_phone': '203-555-1212',
                     'content': 'some data'
                    })
        self.assertTrue(form.is_valid())

        resp = self.client.get(reverse("contact"))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(ContactView.as_view().__name__, resp.resolver_match.func.__name__)
        self.assertTemplateUsed(resp, template_name='base.html')
        self.assertTemplateUsed(resp, template_name='contact.html')
                                   

    def test_contact_form_email_input(self):
        form_data = {'contact_name': 'Kevin', 
                     'contact_email': 'kevin@example.com',
                     'contact_phone': '203-345-1234',
                     'content': 'some data'
                    }
        #form = ContactForm(data=form_data)
        form = ContactForm(form_data)
        self.assertFieldOutput(EmailField, {'a@a.com': 'a@a.com'}, {'aaa': ['Enter a valid email address.']})

    """
    def test_forms(self):
        form_data = {'contact_name': 'Kevin', 
                     'contact_email': 'kevin@example.com',
                     'contact_phone': '203-345-1234',
                     'content': 'some data'
                    }
        response = self.client.post("form", form_data)
        self.assertFormError(response, 'form', 'something', 'This field is required.')

        #response = self.client.get(reverse("helloworld:error_as_404"))

    """
class Test404Error(TestCase):
    def test_404_error_is_raised(self):
        response = self.client.get(reverse("error_as_404"))
        self.assertEqual(404, response.status_code)


