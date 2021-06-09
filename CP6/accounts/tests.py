from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.
class TestUser(TestCase):
    def test_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='testuser',
            email='testemail@yopmail.com',
            first_name='testfirst',
            last_name='testlast',
            age=22,
            is_staff=True,
            is_superuser=False,
            
        )

        self.assertEqual(user.username,'testuser')
        self.assertEqual(user.email,'testemail@yopmail.com')
        self.assertEqual(user.first_name,'testfirst')
        self.assertEqual(user.last_name,'testlast')
        self.assertEqual(user.age,22)
        self.assertTrue(user.is_staff)
        self.assertFalse(user.is_superuser)

    
    def test_super_user(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            username='testadminuser',
            email='testadmin@yopmail.com',
            first_name='firstadmin',
            last_name='lastadmin',
            age=22,
            is_staff=True,
            is_superuser=True,

            
        )

        self.assertEqual(user.username,'testadminuser')
        self.assertEqual(user.email,'testadmin@yopmail.com')
        self.assertEqual(user.first_name,'firstadmin')
        self.assertEqual(user.last_name,'lastadmin')
        self.assertEqual(user.age,22)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
