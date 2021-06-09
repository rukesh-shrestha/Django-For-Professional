from django.test import TestCase
from django.contrib.auth import get_user_model
from django.test.testcases import SimpleTestCase
from django.urls import reverse
from django.urls.base import resolve
from .views import SignUpPage
from django.contrib.auth import views



# Create your tests here.
class UserTest(TestCase):
    def test_user_model(self):
        User = get_user_model()
        user = User.objects.create_user(
            username ='rukesh',
            email = 'rukesh.shrestha11@gmail.com',
            age = 23,
            first_name = 'rukesh',
            last_name = 'shrestha',
            is_staff = True,
            password = 'rukeshshrestha'

        )

        self.assertEqual(user.username,'rukesh')
        self.assertEqual(user.email,'rukesh.shrestha11@gmail.com')
        self.assertEqual(user.age,23)
        self.assertEqual(user.first_name,'rukesh')
        self.assertEqual(user.last_name,'shrestha')
        self.assertTrue('is_staff')

    def test_superuser_model(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            username = 'adminrukesh',
            email = 'adminrukesh@gmail.com',
            age = 25,
            first_name = 'adminadmin',
            last_name = 'adminadmin',
            password = 'adminrukeshadmin'
        )

        self.assertEqual(user.username,'adminrukesh'),
        self.assertEqual(user.email,'adminrukesh@gmail.com'),
        self.assertNotEqual(user.age,23),
        self.assertEqual(user.first_name,'adminadmin'),
        self.assertEqual(user.last_name,'adminadmin')


class UserPagesTest(SimpleTestCase):
    def setUp(self):
        urlsignup = reverse('signup')
        urlsignin = reverse('login')
     
        self.responsesgnup = self.client.get(urlsignup)
        self.responseurlsgnup = self.client.get('/accounts/signup/')
        self.responsesgnin = self.client.get(urlsignin)
        self.responseurlsgnin = self.client.get('/accounts/login/')
        
        
    
    def test_signup_page_url(self):
        self.assertEqual(self.responseurlsgnup.status_code,200)

    def test_signup_page_reverse(self):
        self.assertEqual(self.responsesgnup.status_code,200)
    
    def test_signup_page_template(self):
        self.assertTemplateUsed(self.responsesgnup,'signup.html')
        self.assertTemplateUsed(self.responseurlsgnup,'signup.html')
    
    def test_signup_view_function(self):
        view = resolve('/accounts/signup/')
        self.assertEqual(
            view.func.__name__,
            SignUpPage.as_view().__name__
        )

    def test_signin_page_url(self):
        self.assertEqual(self.responseurlsgnin.status_code,200)

    def test_sigin_page_reverse(self):
        self.assertEqual(self.responsesgnin.status_code,200)

    def test_signin_page_template(self):
        self.assertTemplateUsed(self.responsesgnin,'registration/login.html')
        self.assertTemplateUsed(self.responseurlsgnin,'registration/login.html')

    def test_signin_page_function(self):
        view = resolve('/accounts/login/')
        self.assertEqual(
            view.func.__name__,
            views.LoginView.as_view().__name__

        )


    
