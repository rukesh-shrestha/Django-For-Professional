from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.
class UserTest(TestCase):
    def test_user_model(self):
        User = get_user_model()
        user = User.objects.create_user(
            username = 'rukesh',
            email = 'rukesh.shrestha11@gmail.com',
            first_name = 'rukesh',
            last_name = 'shrestha',
            age = 23,
            is_staff = True
        )

        self.assertEqual(user.username,'rukesh')
        self.assertEqual(user.email,'rukesh.shrestha11@gmail.com')
        self.assertEqual(user.first_name,'rukesh')
        self.assertEqual(user.last_name,'shrestha')
        self.assertEqual(user.age,23)
        self.assertTrue(user.is_staff)

    def test_user_admin(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            username='admin',
            email='admin@yopmail.com',
            password='adminadmin',
            age=22

        )

        self.assertEqual(user.username,'admin')
        self.assertEqual(user.email,'admin@yopmail.com')
        self.assertEqual(user.age,22)

