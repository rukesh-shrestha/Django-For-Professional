from django.test import SimpleTestCase
from django.urls import reverse,resolve
from .views import HomePageView,AboutPageView
from django.contrib.auth.views import LoginView
from accounts.views import SignupPageView


# Create your tests here.
class TestPages(SimpleTestCase):
    def setUp(self):
        homes = reverse('home')
        self.homerepsonse = self.client.get(homes)
        self.homeresponseurl = self.client.get('/')

        login = reverse('login')
        self.loginreverse = self.client.get(login)
        self.loginreverseurl = self.client.get('/accounts/login/')

        signup = reverse('signup')
        self.signupreverse = self.client.get(signup)
        self.signupreverseurl = self.client.get('/accounts/signup/')

        aboutus = reverse('about')
        self.aboutusreverse = self.client.get(aboutus)
        self.aboutusurl = self.client.get('/about/')


    def test_home_reverse(self):
        self.assertEqual(self.homerepsonse.status_code,200)

    def test_home_url(self):
        self.assertEqual(self.homeresponseurl.status_code,200)

    def test_home_template(self):
        self.assertTemplateUsed(self.homeresponseurl,'home.html')
        self.assertTemplateUsed(self.homerepsonse,'home.html')

    def test_home_function(self):
        view = resolve('/')
        self.assertEqual(
            view.func.__name__,
            HomePageView.as_view().__name__

        
        )

    def test_login_reverse(self):
        self.assertEqual(
            self.loginreverse.status_code,
            200
        )

    def test_login_reverseurl(self):
        self.assertEqual(
            self.loginreverseurl.status_code,
            200
        )

    def test_login_template(self):
        self.assertTemplateUsed(
            self.loginreverseurl,
            'registration/login.html'
        )

        self.assertTemplateUsed(
            self.loginreverse,
            'registration/login.html'
    )

    def test_login_function(self):
        view = resolve('/accounts/login/')
        self.assertEqual(
            view.func.__name__,
            LoginView.as_view().__name__

        )

    def test_signup_reverse(self):
        self.assertEqual(
            self.signupreverse.status_code,
            200
        )

    def test_signup_url(self):
        self.assertEqual(
            self.signupreverseurl.status_code,
            200
        )

    def test_signup_template(self):
        self.assertTemplateUsed(
            self.signupreverseurl,
            'signup.html'
        )

        self.assertTemplateUsed(
            self.signupreverse,
            'signup.html'
        )

    def test_signup_funtion(self):
        view = resolve('/accounts/signup/')
        self.assertEqual(
            view.func.__name__,
            SignupPageView.as_view().__name__

        )


    def test_about_reverse(self):
        self.assertEqual(
            self.aboutusreverse.status_code,
            200
        )
    
    def test_about_url(self):
        self.assertEqual(
            self.aboutusurl.status_code,
            200
        )

    def test_about_template(self):
        self.assertTemplateUsed(
            self.aboutusurl,
            'about.html'
        )

        self.assertTemplateUsed(
            self.aboutusreverse,
            'about.html'
        )


    def test_about_function(self):
        view = resolve('/about/')
        self.assertEqual(
            view.func.__name__,
            AboutPageView.as_view().__name__
        )

        




