import smtplib
import socket

import mock

from tests.base import AppTest, MINIMALIST_MAIL


class MockSMTP:

    inst = mock.MagicMock()

    def __enter__(self):
        return self.inst

    def __exit__(self, *args):
        pass


class MailResourceTest(AppTest):

    def setUp(self):
        super().setUp()
        socket.create_connection = mock.MagicMock()
        self.mocked_connect = smtplib.SMTP_SSL = mock.MagicMock()
        self.mocked_close = smtplib.SMTP_SSL.close = mock.MagicMock()
        self.mocked_send = smtplib.SMTP_SSL.send = mock.MagicMock()
        self.mocked_getreply = smtplib.SMTP_SSL.getreply = mock.MagicMock()

        self.mocked_connect.return_value = (220, "Ok")
        self.mocked_getreply.return_value = (221, "Ok")

    def test_resource_accepted_methods(self):
        self.app.get('/mail', status=405)
        self.app.put('/mail', status=405)
        self.app.patch('/mail', status=405)
        self.app.delete('/mail', status=405)

    def test_send_validates_body(self):
        response = self.app.post('/mail', {}, status=400)
        self.assertIn('errors', response.json)

    @mock.patch('edwiges.views.SMTP_SSL')
    def test_send_starts_smtp_ssl(self, mocked):
        self.app.post('/mail', MINIMALIST_MAIL, status=200)
        host = self.settings['edwiges.provider_host']
        port = self.settings['edwiges.provider_port']
        mocked.assert_called_once_with(host, port)
