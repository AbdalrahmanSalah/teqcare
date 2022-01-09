from django.test import TestCase , Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email= "testadmin@teqniea.com",
            password= "test123"
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email= "testnotanadmin@teqniea.com",
            password= "test123",
            name= "abdelrahman salah ahmed"
        )

    # def test_users_listed(self):
    #     """Test that users are listed on user page"""
    #     url = reverse('admin:core_user_changelist')
    #     response = self.client.get(url)
    #
    #     # self.assertContains(response, self.user.name)
    #     self.assertEqual(response, self.user.email)
