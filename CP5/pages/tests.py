from pages.views import HomePage
from django.test import SimpleTestCase
from django.urls import reverse,resolve

# Create your tests here.
class HomePageTest(SimpleTestCase):
    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)
        self.responseurl = self.client.get('/')

    def test_home_page_reverse(self):
        self.assertEqual(self.response.status_code,200)
    def test_home_page_reverse_template(self):
        self.assertTemplateUsed(self.response,'home.html')
    def test_home_page_url(self):
        self.assertEqual(self.responseurl.status_code,200)
    def test_home_page_view_function(self):
        view = resolve('/')
        self.assertEqual(
            view.func.__name__,
            HomePage.as_view().__name__

        )