import unittest
import os
os.environ['TESTING'] = 'true'

from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>MLH Fellow</title>" in html

    def test_home_about(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "About Me" in html
    
    def test_home_work(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "Work Experience" in html

    def test_home_education(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "My Education" in html

    def test_timeline(self):
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 0
    
    def test_timeline_page_title(self):
        response = self.client.get("/timeline")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "Timeline" in html

    def test_timeline_page_create(self):
        response = self.client.get("/timeline")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "New Post" in html

    def test_timeline_create(self):
        response = self.client.post("/api/timeline_post", data={"name": "TEST t1m3linE", "email": "a@a.com", "content": "aa"})
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert json["name"] == "TEST t1m3linE"
        assert json["email"] == "a@a.com"
        assert json["content"] == "aa"

        response = self.client.post("/api/timeline_post", data={"name": "TEST 2", "email": "b@a.com", "content": "aa"})
        assert response.status_code == 200
        assert response.is_json

        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "TEST t1m3linE" in str(json)
        assert len(json["timeline_posts"]) >= 1

        for obj in json["timeline_posts"]:
          if obj["name"] == "TEST t1m3linE":
            assert obj["email"] == "a@a.com"
            assert obj["content"] == "aa"
            return
        
        assert False

    def test_malformed_timeline_post(self):
        # POST request missing name
        response = self.client.post("/api/timeline_post", data={"email": "john@example.com", "content": "Hello world, I'm John!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid name" in html

        # POST request with empty content
        response = self.client.post("/api/timeline_post", data={"name": "John Doe", "email": "john@example.com", "content": ""})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid content" in html

        # POST request with malformed email
        response = self.client.post("/api/timeline_post", data={"name": "John Doe", "email": "not-an-email", "content": "Hello world, I'm John!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid email" in html
