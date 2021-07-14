from django.test import TestCase
from .models import CustomUser
from django.contrib.auth import get_user_model


# Create your tests here.

class user_test(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'omar',
            email = 'omar@gmail.com',
            password = 'obada19947'

        )

    def test_user_creation(self):
        self.assertEquals(self.user.__str__(),'omar') 

    def test_duplicates(self):
        try:
            self.user2 = get_user_model().objects.create_user(

                username = 'omar',
                email = 'omar@gmail.come',
                password = 'obada19947'

            )
        
        except:
            print('falled')

    

