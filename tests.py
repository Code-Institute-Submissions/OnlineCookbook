from app import *
import unittest

testapp = app.test_client()

class TestStringMethods(unittest.TestCase):
    
    def set_up(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_is_this_thing_on(self):
        """ Test that testing is working properly """
        self.assertEqual(1, 1)
    
    def test_home_status(self):
        """ Test status code of home page
        """
        with app.test_client() as client:
            response = client.get('/')
            self.assertEqual(response.status_code, 200)
    
    def test_bad_route(self):
        """ Test status code of home page
        """
        with app.test_client() as client:
            response = client.get('/kjhsdkfhksdhjfkhf')
            self.assertEqual(response.status_code, 404)
    