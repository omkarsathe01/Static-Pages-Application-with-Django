# pages/tests.py
from django.test import SimpleTestCase, TestCase

# Create your tests here.


class PageTests(SimpleTestCase):

  def test_home_page_status_code(self):
    response = self.client.get('/')
    self.assertEqual(response.status_code, 200)

  def test_about_page_status_code(self):
    response = self.client.get('/about/')
    self.assertEqual(response.status_code, 200)