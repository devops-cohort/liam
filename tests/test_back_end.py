import unittest

from flask import abort, url_for
from flask_testing import TestCase
from os import getenv
from application import app, db
from application.models import shen_user, shen_gong

class TestBase(TestCase):

    def create_app(self):

        # pass in test configurations
        config_name = 'testing'
        app.config.update(
            SQLALCHEMY_DATABASE_URI='mysql+pymysql://'+str(getenv('MYSQL_USER'))+':'+str(getenv('MYSQL_PASSWORD'))+'@'+st$
        )
        return app

    def setUp(self):
        """
        Will be called before every test
        """

        db.session.commit()
        db.drop_all()
        db.create_all()

        # create test admin user
        admin = shen_user(username="admin", email="admin@admin.com", password="admin2016")

        # create test non-admin user
        user = shen_user(username="user", email="test@user.com", password="test2016")

        # save users to database
        db.session.add(admin)
        db.session.add(employee)
        db.session.commit()

    def tearDown(self):
        """
        Will be called after every test
        """

        db.session.remove()
        db.drop_all()

class ViewTest(TestBase):
    def test_homepage_view(self):
        response =self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_aboutpage_view(self):
        response =self.client.get(url_for('about'))
        self.assertEqual(response.status_code, 200)

    def test_registerpage_view(self):
        response =self.client.get(url_for('register'))
        self.assertEqual(response.status_code, 200)

    def test_postpage_view(self):
        response =self.client.get(url_for('post'))
        self.assertEqual(response.status_code, 200)

    def test_accountpage_view(self):
        response =self.client.get(url_for('account'))
        self.assertEqual(response.status_code, 302)

    def test_loginpage_view(self):
        response =self.client.get(url_for('login'))
        self.assertEqual(response.status_code, 200)

    def test_userlogin_view(self):
        target_url = url_for('user', id=2)
        redirect_url = url_for('login', next=target_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, redirect_url)

    def test_userregister_view(self):
        target_url = url_for('user', id=2)
        redirect_url = url_for('register', next=target_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, redirect_url)

class ModelTest(TestBase):

    def test_user_model(self):
        user = User(first_name="yeet", last_name="yeet", email="yeet@gmail.com", password="yeet1")

        db.session.add(user)
        db.session.commit()

        self.assertEqual(User.query.count(), 3)

    def test_posts_model(self):
        post = Posts(title="Sir", content="abcdefghijklmnopqrstivwyz")
        db.session.add(post)
        db.session.commit()
