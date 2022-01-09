from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email_and_password(self):
        """test creating a new user with an email and a password """
        email = 'TEQCare@teqnia.com'
        password = 'TestPass123'
        user = get_user_model().objects.create_user(
        email=email,
        password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """test the email for new user is normalized"""
        email = 'test@EGYPTCAPPEV.COM'
        user = get_user_model().objects.create_user(email,'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raise an error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None , 'test123')

    def test_create_suberuser(self):
        """Test creating suberuser"""
        user = get_user_model().objects.create_superuser(
        "test@teqniea.com",
        "test123"
        )

        self.assertTrue(user.is_suberuser)
        self.assertTrue(user.is_staff)
