from unittest import TestCase
from server import app
from model import connect_to_db, db
from flask import session


class FlaskTests(TestCase):
    """Tests for the Flask server"""

    def setUp(self):
        """Setup before every test."""

        # Get the Flask test client
        self.client = app.test_client()

        # Show Flask errors that happen during tests
        app.config['TESTING'] = True


    def test_homepage(self):
        """Test homepage"""

        result = self.client.get("/")
        self.assertIn(b"Welcome!", result.data)


    def test_login(self):
        """Test login route"""

        result = self.client.post("/login",
                                  data={"user_id": "tester", "password": "test"},
                                  follow_redirects=True)
        self.assertIn(b"Logged in as", result.data)


class FlaskTestsDatabase(TestCase):
    """Flask tests that use the database."""

    def setUp(self):
        """Setup before every test."""

        # Get the Flask test client
        self.client = app.test_client()
        app.config['TESTING'] = True

        # Connect to test database
        connect_to_db(app, "postgresql:///testrejuvenate")

        # Create tables and add sample data
        db.create_all()
        example_data()


    def tearDown(self):
        """Do at end of every test."""

        db.session.remove()
        db.drop_all()
        db.engine.dispose()


    def test_all_recipes(self):
        """Test recipes page."""

        result = self.client.get("/recipes")
        self.assertIn(b"Recipes", result.data)


    def test_recipe_details(self):
        """Test recipe details page."""

        result = self.client.get("/recipes/<recipe_id>")
        self.assertIn(b"", result.data)


class FlaskTestsLoggedIn(TestCase):
    """Flask tests with user logged in to session."""

    def setUp(self):
        """Stuff to do before every test."""

        app.config['TESTING'] = True
        app.config['SECRET_KEY'] = 'key'
        self.client = app.test_client()

        with self.client as c:
            with c.session_transaction() as sess:
                sess['user_id'] = 1


    def test_profile_page(self):
        """Test profile page."""

        result = self.client.get("/profile")
        self.assertIn(b"You are a valued user", result.data)


class FlaskTestsLoggedOut(TestCase):
    """Flask tests with user logged in to session."""

    def setUp(self):
        """Stuff to do before every test."""

        app.config['TESTING'] = True
        self.client = app.test_client()


    def test_profile_page(self):
        """Test that user can't see profile page when logged out."""

        result = self.client.get("/profile", follow_redirects=True)
        self.assertNotIn(b"You are a valued user", result.data)
        self.assertIn(b"You must be logged in", result.data)


class FlaskTestsLogInLogOut(TestCase):  # Bonus example. Not in lecture.
    """Test log in and log out."""

    def setUp(self):
        """Before every test"""

        app.config['TESTING'] = True
        self.client = app.test_client()


    def test_login(self):
        """Test log in form.

        Unlike login test above, 'with' is necessary here in order to refer to session.
        """

        with self.client as c:
            result = c.post('/login',
                            data={'user_id': '42', 'password': 'tester'},
                            follow_redirects=True
                            )
            self.assertEqual(session['user_id'], '42')
            self.assertIn(b"You are a valued user", result.data)


    def test_logout(self):
        """Test logout route."""

        with self.client as c:
            with c.session_transaction() as sess:
                sess['user_id'] = '42'

            result = self.client.get('/logout', follow_redirects=True)

            self.assertNotIn(b'user_id', session)
            self.assertIn(b'Logged Out', result.data)


if __name__ == "__main__":
    import unittest

    unittest.main()