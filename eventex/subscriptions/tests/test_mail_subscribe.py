from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Alan Maik', cpf='12345678901',
                    email='alanmaikm@gmail.com', phone='73-99955-8094')
        self.client.post('/inscricao/', data)
        self.email =mail.outbox[0]
    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'
        self.assertEqual(expect, self.email.subject)
    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'
        self.assertEqual(expect, self.email.from_email)
    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br','alanmaikm@gmail.com']
        self.assertEqual(expect , self.email.to)
    def test_subscription_email_body(self):
        contents = ['Alan Maik','12345678901','alanmaikm@gmail.com','73-99955-8094']
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)