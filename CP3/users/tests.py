from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.
class CustomUserTest(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='rukesh',
            email = 'rukesh.shrestha11@gmail.com',
            first_name='rukesh',
            last_name='shrestha',
            age=23,
            password='adminadmin',
            is_staff=True
            
        )

        self.assertEqual(user.username,'rukesh')
        self.assertEqual(user.email,'rukesh.shrestha11@gmail.com')
        self.assertEqual(user.first_name,'rukesh')
        self.assertEqual(user.last_name,'shrestha')
        self.assertEqual(user.age,23)
        self.assertTrue(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertTrue(user.is_active)

    def test_admin_user(self):
        User=get_user_model()
        adminuser=User.objects.create_superuser(
            username='admin',
            email='admin@yopmail.com',
            age=22,
            first_name='adminuser',
            last_name='adminlastuser',
            password='adminadmin'

        )

        self.assertEqual(adminuser.username,'admin')
        self.assertEqual(adminuser.email,'admin@yopmail.com')
        self.assertEqual(adminuser.age,22)
        self.assertEqual(adminuser.first_name,'adminuser')
        self.assertEqual(adminuser.last_name,'adminlastuser')
        self.assertTrue(adminuser.is_superuser)
        self.assertTrue(adminuser.is_active)