import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from app.hobby import Hobbies, Hobby
from app.education import EducationExperience, EducationHistory
from app.visited import PlaceVisited, PlacesVisited
from peewee import *

load_dotenv()
app = Flask(__name__)

mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
              user=os.getenv("MYSQL_USER"),
              password=os.getenv("MYSQL_PASSWORD"),
              host=os.getenv("MYSQL_HOST"),
              port=3306
 )

print(mydb)

class TimelinePost(Model):
  name = CharField()
  email = CharField()
  content = TextField()
  created_at = DateTimeField(defualt=datetime.datetime.now)

  class Meta:
    database = mydb

mydb.connect()
mydb.create_tables([TimelinePost])

@app.route('/api/timeline_post', method=['POST'])
def post_time_line_post():
  name = request.form['name']
  email = request.form['email']
  content = request.form['content']
  timeline_post = TimelinePost.create(name=name, email=email, content=content)

  return model_to_dict(timeline_post)

@app.route('/api/timeline_post', method=['GET'])
def get_time_line_post():
  return {
    'timeline_posts': [
      model_to_dict(p)
      for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
    ]
  }


# Variable declarations for texts
title = "Young Chen"

photo = "./static/img/profile.jpg"

aboutMeGreetings = "Hello There! I'm Young"
aboutMeDescription = "I'm currently an MLH Fellow specializing in Production Engineering. I thrive on solving complex problems, optimizing systems, and ensuring the reliability and scalability of web applications. With a strong foundation in software engineering principles and hands-on experience in deploying and managing production systems, I am committed to delivering high-quality, efficient solutions."
workExperience = [
    {
        "id": 0,
        "title": "MLH Production Engineer Fellow",
        "company": "Major League Hacking",
        "date": "June 2024 - Present",
        "description": "Participated in a fellowship program focused on site reliability engineering and DevOps. Implemented CI/CD pipelines, monitored system performance, and collaborated with a global team to improve application scalability and reliability.",
        "image": "./static/img/MLH_logo.png"
    },
    {
        "id": 1,
        "title": "Teaching Assistant",
        "company": "University of Toronto",
        "date": "September 2022 - Present",
        "description": "Lead tutorials for a class of 30, helping to provide student with practical examples of the course material. Increased the tutorial’s course average by around 10% compared to the overall course average. Taught Calculus 1 & 2 for Physical Sciences and Calculus 2 for Management.",
        "image": "./static/img/uoft.png"
    },
    {
        "id": 2,
        "title": "Software Developer Intern",
        "company": "AutoTrader",
        "date": "September 2022 - April 2023",
        "description": "Developed Jetpack Compose components for internal APIs, allowing for an 80\% increase of developer efficiency through the use of modularity and reusability. Worked in an Agile environment by tracking tasks on a Kanban board and resolving blockers during daily standups. Improved the user experience of 1,400,000 users by developing application enhancements and bug fixes.",
        "image": "./static/img/auto.jpeg"
    }

]
numOfJobs = len(workExperience)



hobbies = Hobbies(hobbies = [
  Hobby(
      title = "3D Printing",
      description = "Recently, I've been creating 3D models and printing them.",
      images = [
          "./static/img/3d.jpg"
      ]
  ),
  Hobby(
      title = "Photography",
      description = "I like taking photos of stuff.",
      images = [
          "./static/img/bagcam.jpg"
      ]
  ),
])

education = EducationHistory([
    EducationExperience(
        title = "Bachelor of Science in Computer Science",
        school = "University of Toronto",
        description = ["3.6/4.0 GPA", "Awards: University of Toronto Scholar, Dean's List 2023"],
        date = "2021 - 2025",
        logo = "https://upload.wikimedia.org/wikipedia/en/thumb/0/04/Utoronto_coa.svg/1280px-Utoronto_coa.svg.png"
    ),
    EducationExperience(
        title = "Ontario Secondary School Degree (OSSD)",
        school = "Pierre Elliott Trudeau High School",
        description = ["97% Average", "Awards: Ontario Scholar", "Clubs: CS Club, Mathematica, Game Design Club"],
        date = "2017 - 2021",
        logo = "https://upload.wikimedia.org/wikipedia/en/thumb/0/04/Utoronto_coa.svg/1280px-Utoronto_coa.svg.png"
    ),
])

places_visited = PlacesVisited([
    PlaceVisited(
        title = "Niagara Falls",
        description = "This winter, I went to Niagara Falls to see the waterfall.",
        url = """https://maps.google.com/maps?width=100%25&amp;height=600&amp;hl=en&amp;q=niagara%20falls+(My%20Business%20Name)&amp;t=&amp;z=14&amp;ie=UTF8&amp;iwloc=B&amp;output=embed"""
    ),
    PlaceVisited(
        title = "Mont Tremblant",
        description = "Last winter, I drove 10 hours to go skiing at Mont Tremblant near Montreal.",
        url = """https://maps.google.com/maps?width=100%25&amp;height=600&amp;hl=en&amp;q=mont%20tremblant+()&amp;t=&amp;z=14&amp;ie=UTF8&amp;iwloc=B&amp;output=embed"""
    ),
    PlaceVisited(
        title = "CN Tower",
        description = "A few months ago, I went up the CN Tower to see the Toronto skyline.",
        url = """https://maps.google.com/maps?width=100%25&amp;height=600&amp;hl=en&amp;q=cn%20tower+()&amp;t=&amp;z=14&amp;ie=UTF8&amp;iwloc=B&amp;output=embed"""
    )
])

@app.route('/')
def index():
    return render_template(
        'index.html',
        title = "MLH Fellow",
        photo = photo,
        aboutMeGreetings = aboutMeGreetings,
        aboutMeDescription = aboutMeDescription,
        workExperience = workExperience,
        numOfJobs = numOfJobs,
        hobbies = hobbies,
        education = education,
        placesVisited = places_visited,
        url=os.getenv("URL")
    )

@app.route('/visited_page.html')
def visited_page():
    return render_template(
        'visited_page.html',
        title = "MLH Fellow",
        photo = photo,
        aboutMeGreetings = aboutMeGreetings,
        aboutMeDescription = aboutMeDescription,
        workExperience = workExperience,
        numOfJobs = numOfJobs,
        hobbies = hobbies,
        education = education,
        placesVisited = places_visited,
        url=os.getenv("URL")
    )

@app.route('/hobbies_page.html')
def hobbies_page():
    return render_template(
        'hobbies_page.html',
        title = "MLH Fellow",
        photo = photo,
        aboutMeGreetings = aboutMeGreetings,
        aboutMeDescription = aboutMeDescription,
        workExperience = workExperience,
        numOfJobs = numOfJobs,
        hobbies = hobbies,
        education = education,
        placesVisited = places_visited,
        url=os.getenv("URL")
    )
