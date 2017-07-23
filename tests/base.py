import os

from webtest import TestApp
import unittest

from edwiges import main

__dir_path = os.path.dirname(__file__)

TEST_IMAGE = "{}/test_image.jpg".format(__dir_path)
TEST_IMAGE_CONTENT = open(TEST_IMAGE, 'rb').read()

MINIMALIST_MAIL = {
    "sender": "harry@loggi.com",
    "recipients": ["hagrid@hogwarts.edu", "hermione@magic.gov.uk"],
    "subject": "Umbridge memes",
    "body": "Hue",
}


FULL_MAIL = MINIMALIST_MAIL.copy()
FULL_MAIL.update(**{
    "reply_to": "suport@loggi.com",
    "attachments": [
        {
            "filename": "meme.jpg",
            "content": TEST_IMAGE_CONTENT,
        }
    ],
})


class AppTest(unittest.TestCase):

    @property
    def global_config(cls):
        return {}

    @property
    def settings(cls):
        return {
            "edwiges.provider_host": "localhost",
            "edwiges.provider_port": "465",
            "edwiges.provider_username": "root",
            "edwiges.provider_password": "pass",
        }

    def setUp(self):
        self.app = TestApp(main(self.global_config, **self.settings))
