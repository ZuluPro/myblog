from django.test import TestCase
from django.core.urlresolvers import reverse


class ViewAboutMeTest(TestCase):
    fixtures = (
        'initial_data',
    )

    def test_view(self):
        url = reverse('aboutme')
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
