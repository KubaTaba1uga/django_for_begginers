from django.test import SimpleTestCase


class Response200(SimpleTestCase):
    """
    Ensures that pages which should be returning 200, are doing it 
    """
    def test_hello_word_page_status_code(self):
        response = self.client.get('/hello_world')
        self.assertEqual(response.status_code, 200)

    def test_about_me_page_status_code(self):
        response = self.client.get('/about_me')
        self.assertEqual(response.status_code, 200)
