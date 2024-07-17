
import unittest
import os
os.environ["TESTING"] = "True"

from app import app

class AppTestCase(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get('/')
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>MLH Fellow</title>" in html
        assert '<h1 class="aboutMeTitle">About Me</h1>' in html
        assert '<h1 class="workExperienceTitle">Work Experience</h1>' in html
        assert "<h1>My Education</h1>" in html

    def test_timeline(self):
        # test api get
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 0
        # test api post
        response = self.client.post("/api/timeline_post", data={
            "name": "John Doe",
            "email": "jhon@email.com",
            "content": "Hello World"
        })
        assert response.status_code == 200
        assert 'application/json' in response.content_type
        json_data = response.get_json()
        assert json_data["name"] == "John Doe"
        assert json_data["email"] == "jhon@email.com"
        assert json_data["content"] == "Hello World"
        # test get again
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 1
        post = json["timeline_posts"][0]
        assert post["name"] == "John Doe"
        assert post["email"] == "jhon@email.com"
        assert post["content"] == "Hello World"

        #test timeline page content
        response = self.client.get('/timeline.html')
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>MLH Fellow</title>" in html
        assert '<input type="text" id="name" name="name" required><br><br>' in html

    def test_malformed_timeline_post(self):
        # POST request missing name
        response = self.client.post("/api/timeline_post", data=
        {"email": "john@example.com", "content": "Hello world, I'm John!"})
        assert response.status_code == 400
        html = response. get_data(as_text=True)
        assert "Invalid name" in html
        # POST request with empty content
        response = self.client.post("/api/timeline_post", data=
        {"name" : "John Doe", "email": "john@example.com", "content": ""})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        print("printing")
        print(html)
        assert "Invalid content" in html
        # POST request with malformed email
        response = self.client.post("/api/timeline_post", data=
        {"name": "John Doe", "email": "not-an-email", "content": "Hello world, I'm John! "})
        assert response.status_code == 400
        html = response. get_data(as_text=True)
        assert "Invalid email" in html
