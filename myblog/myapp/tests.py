from io import BytesIO
from django.test import TestCase
from django.conf import settings as s
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.core.management import call_command


class BlogTest(TestCase):
    def test_prism(self):
        """Tests if prism present in HTML."""
        url = reverse('zinnia:entry_archive_index')
        res = self.client.get(url)
        self.assertIn('/prism/prism.js"></script>', res.content)
        self.assertIn('/prism/themes/prism.css"/>', res.content)


class AdminTest(TestCase):
    def setUp(self):
        self.user = User(username='admin', is_superuser=True, is_staff=True)
        self.user.set_password('test')
        self.user.save()
        self.client.login(username='admin', password='test')

    def test_tinymce_script_template(self):
        """Tests TinyMCE script view"""
        url = reverse('tinymce-js', args=['admin/zinnia/entry'])
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
        # good_file = 'myblog/myapp/templates/admin/zinnia/entry/tinymce_textareas.js'
        # used_file = res.templates[0].origin.name
        # is_good_file = used_file.endswith(good_file)
        # self.assertTrue(is_good_file, "Bad used template: '%s'" % used_file)

    def test_tinymce_prism_plugin_form(self):
        url = reverse('tinymce-prism-form')
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)

    # def test_tinymce_prism_plugin_editor_plugin(self):
    #     url = '%s/tiny_mce/plugins/prism/editor_plugin.js' % s.STATIC_URL
    #     res = self.client.get(url)
    #     self.assertEqual(res.status_code, 200)


class CommandSettingsTest(TestCase):
    def test_command(self):
        stdout = BytesIO()
        call_command('settings', stdout=stdout)
