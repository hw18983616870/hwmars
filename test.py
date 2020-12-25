import unittest
import app


class TestHome(unittest.TestCase):
    def setUp(self):
        app.app.testing = True
        self.app = app.app.test_client()

    def test_home(self):
        res = self.app.get('/')
        self.assertEqual(res.status, '200 OK')
        self.assertEqual(res.data, b'Hello, World!')

    def test_hello_user(self):
        name = 'Yngwie'
        res = self.app.get(f'/hello/{name}')
        self.assertEqual(res.status, '200 OK')
        self.assertIn(bytearray(f'{name}', 'utf-8'), res.data)


if __name__ == '__main__':
    import xmlrunner
    runner = xmlrunner.XMLTestRunner(output='test-reports')
    unittest.main(testRunner=runner)
    unittest.main()

