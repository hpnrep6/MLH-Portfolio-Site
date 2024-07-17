import unittest
from peewee import *

from app import TimelinePost
MODELS = [TimelinePost]

test_db = SqliteDatabase(':memory:')

class testTimelinePost(unittest.TestCase):
    def setUp(self):
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)

        test_db.connect()
        test_db.create_tables(MODELS)

    def tearDown(self):
        test_db.drop_tables(MODELS)
        test_db.close()

    def test_timeline_post(self):
        #create a couple of posts
        first_post = TimelinePost.create(name='John Doe', email='jhon@hotmail.com', content='Hellow world, im jhon')
        assert first_post.id == 1
        second_post = TimelinePost.create(name='Jane Doe', email='jane@hotmail.com', content='Hellow world, im jane')
        assert second_post.id == 2

        # get timeline posts and check if they are correct
        # get all posts on the timeline
        posts = TimelinePost.select()
        assert posts.count() == 2
        #check first post
        post = posts[0]
        assert post.name == 'John Doe'
        assert post.email == 'jhon@hotmail.com'
        assert post.content == 'Hellow world, im jhon'
        assert post.id == 1
        #check second post
        post = posts[1]
        assert post.name == 'Jane Doe'
        assert post.email == 'jane@hotmail.com'
        assert post.content == 'Hellow world, im jane'
        assert post.id == 2
