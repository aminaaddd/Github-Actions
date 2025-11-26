import unittest
from hello_world import app, greet, generate_html


class TestHelloWorld(unittest.TestCase):

    def setUp(self):
        # Create a test version of the Flask app
        self.client = app.test_client()
        self.client.testing = True

    # ------------ TEST greet() ------------
    def test_greet_function(self):
        result = greet()
        self.assertIsInstance(result, str)
        self.assertIn("Welcome", result)
        self.assertEqual(result, "Welcome to CI/CD 101 using GitHub Actions!")

    # ------------ TEST generate_html() ------------
    def test_generate_html(self):
        msg = "Hello Test"
        html = generate_html(msg)

        self.assertIn("<html>", html)
        self.assertIn(msg, html)               # message should appear in HTML
        self.assertIn("GitHub_Actions", html)  # image exists
        self.assertTrue(html.startswith("\n        <html>"))

    # ------------ TEST /greeting ENDPOINT ------------
    def test_greeting_route(self):
        response = self.client.get("/greeting")

        # HTTP status
        self.assertEqual(response.status_code, 200)

        # Content type
        self.assertEqual(response.content_type, "text/html; charset=utf-8")

        # Check greeting text is included
        self.assertIn(b"Welcome to CI/CD 101 using GitHub Actions!",
                      response.data)

        # Check HTML structure
        self.assertIn(b"<html>", response.data)
        self.assertIn(b"</html>", response.data)

    # ------------ TEST 404 for unknown routes ------------
    def test_unknown_route(self):
        response = self.client.get("/unknown")

        # Flask returns 404 for unknown paths
        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
