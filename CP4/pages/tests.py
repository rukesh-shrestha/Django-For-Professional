from pages.views import HomePage
from django.http import response
from django.test import SimpleTestCase
from django.urls import reverse,resolve

# Create your tests here.
class HomePageTest(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code,200)

    def test_home_page_status_code_reverse(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)

    def test_home_page_template_used(self):
        response_url = self.client.get('/')
        response_reverse = self.client.get(reverse('home'))
        self.assertTemplateUsed(response_url,'home.html')
        self.assertTemplateUsed(response_reverse,'home.html')

    def test_home_page_fuction_resolve(self):
        view = resolve('/')
        self.assertEqual(
            view.func.__name__,
            HomePage.as_view().__name__
        )
    

class HomePageTestUsingSetUp(SimpleTestCase):
    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_home_page_code_setup(self):
        self.assertEqual(self.response.status_code,200)
    def test_home_page_template_setup(self):
        self.assertTemplateUsed(self.response,'home.html')
    
