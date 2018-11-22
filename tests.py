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
        print("Test 'test_is_this_thing_on' has passed")
        
    
    """ Tests the status of the home page and subsequent pages return a code 200, which implies they are working correctly, and not a 404 code """
    def test_page_status(self):
        with app.test_client() as client:
            
            response = client.get('/')
            self.assertEqual(response.status_code, 200)
            self.assertNotEqual(response.status_code, 404)
            
            response = client.get('/all_recipes')
            self.assertEqual(response.status_code, 200)
            self.assertNotEqual(response.status_code, 404)
            
            response = client.get('/add_recipe')
            self.assertEqual(response.status_code, 200)
            self.assertNotEqual(response.status_code, 404)
            
            response = client.get('/add_author')
            self.assertEqual(response.status_code, 200)
            self.assertNotEqual(response.status_code, 404)
        
            
            # The following tests include working id numbers from my database, as required by the url
            response = client.get('/search_veg/5b66ce3ffb6fc06798a136c4')
            self.assertEqual(response.status_code, 200)
            self.assertNotEqual(response.status_code, 404)
            
            response = client.get('/search_cuisine/5b572736fe56dc36e91a3958')
            self.assertEqual(response.status_code, 200)
            self.assertNotEqual(response.status_code, 404)
            
            response = client.get('/search_author/5b66beccfb6fc06798a13192')
            self.assertEqual(response.status_code, 200)
            self.assertNotEqual(response.status_code, 404)
            
        print("Test 'test_page_status' has passed")
        
            
            
    """ Tests that a route which is not a working path returns an error message with a status code 404, and not a status code 200 """
    def test_bad_route(self):
        with app.test_client() as client:
            response = client.get('/kjhsdkfhksdhjfkhf')
            self.assertEqual(response.status_code, 404)
            self.assertNotEqual(response.status_code, 200)
        print("Test 'test_bad_route' has passed")
            
            
    
    """Tests the get_counts function, with a dummy recipe object"""      
    def test_get_counts(self):
        
        self.test_recipe_object = [{'author_name': 'Scott', 'recipe_name': 'Chilli', 'recipe_ingredients': 'chilli'}, {'author_name': 'Jess', 'recipe_name': 'Omlette', 'recipe_ingredients': 'Eggs'}, {'author_name': 'Jess', 'recipe_name': 'Chicken', 'recipe_ingredients': 'Chicken'}]
        self.test_authors_names = ['sarah', 'scott', 'jess']
        self.test_response =  {'jess': 2, 'sarah': 0, 'scott': 1}
        self.test_response_wrong = {'jess': 3, 'sarah': 0, 'scott': 1}
        
        self.test_recipe_object2 = [{'author_name': 'Pat', 'recipe_name': 'Chilli', 'recipe_ingredients': 'chilli'}, {'author_name': 'Pam', 'recipe_name': 'Omlette', 'recipe_ingredients': 'Eggs'}, {'author_name': '38383', 'recipe_name': 'Chicken', 'recipe_ingredients': 'Chicken'}, {'author_name': 'Pat', 'recipe_name': 'Chilli', 'recipe_ingredients': 'chilli'}, {'author_name': 'Pat', 'recipe_name': 'Chilli', 'recipe_ingredients': 'chilli'}, {'author_name': 'Pat', 'recipe_name': 'Chilli', 'recipe_ingredients': 'chilli'}]
        self.test_authors_names2 = ['pat', 'pam', '38383', 'jess']
        self.test_response2 =  {'pat': 4, 'pam': 1, '38383': 1, 'jess': 0}
        self.test_response_wrong2 =  {'paul': 4, 'james': 1, '383838': 1, 'jess': 0}
        
        
        self.assertEqual((get_counts(self.test_recipe_object, 'author_name', self.test_authors_names)), self.test_response)
        self.assertNotEqual((get_counts(self.test_recipe_object, 'author_name', self.test_authors_names)), self.test_response_wrong)
        
        self.assertEqual((get_counts(self.test_recipe_object2, 'author_name', self.test_authors_names2)), self.test_response2)
        self.assertNotEqual((get_counts(self.test_recipe_object, 'author_name', self.test_authors_names)), self.test_response_wrong2)
        
        print("Test 'test_get_counts' has passed")
            
            
    
if __name__ == '__main__':
    unittest.main()