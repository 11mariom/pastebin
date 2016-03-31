from unittest import TestCase
from pastebin import pastebin

class TestHello(TestCase):

    def setUp(self):
        #pastebin.app.config['TESTING'] = True
        self.app = pastebin.app.test_client()

    def test_hello(self):
        rv = self.app.get("/")
        assert 'hello world' in rv.data

if __name__ == "__main__":
    unittest.main()
