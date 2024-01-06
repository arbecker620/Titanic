import unittest
import requests


class TestRESTMethods(unittest.TestCase):

    def test_valid_url(self):
        r = requests.get('http://127.0.0.1:5000')
        self.assertEqual(200,r.status_code)



if __name__ == '__main__':
    unittest.main()