from django.test import TestCase
from Pyowa.microblog import models

class MicroblogTests(TestCase):

    fixtures = ('test_blog_data', )

    def test_unicode(self):
        blog = models.Microblog.objects.all()[0]
        self.assertEqual(blog.poster.username + ': ' + blog.message, str(blog))