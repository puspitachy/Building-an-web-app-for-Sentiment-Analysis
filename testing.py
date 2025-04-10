import main
import unittest


class MyTestingCase(unittest.TestCase):

    def setUp(self):
        main.app.testing = True
        self.app = main.app.test_client()

    def test_home(self):
        result = self.app.get('/')

        # Testing the behavior of the starting page page
        def test_home(self):
            responses = self.app.get('/home')
            self.assertEqual(responses.status_code, 200)
            self.assertIn(b'Welcome to my sentiment analysis web app!', responses.data)

        # Testing the behavior of the reviewform page
        def test_about(self):
            responses = self.app.get('/reviewform')
            self.assertEqual(responses.status_code, 200)
            self.assertIn(b'This is starting page.', responses.data)

        # Testing the behavior of the form page
        def test_contact(self):
            responses = self.app.get('/form')
            self.assertEqual(responses.status_code, 200)
            self.assertIn('Fine loading', responses.data)
if __name__ == '__main__':
    unittest.main()