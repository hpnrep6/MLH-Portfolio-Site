import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from app.hobby import Hobbies, Hobby
from app.education import EducationExperience, EducationHistory
from app.visited import PlaceVisited, PlacesVisited
from peewee import *
from peewee import Model, CharField, TextField, DateTimeField
import datetime
from playhouse.shortcuts import model_to_dict
import re

load_dotenv('example.env')
app = Flask(__name__)

#DB Config
if os.getenv("TESTING") == "true":
    print("Running in test mode")
    mydb = SqliteDatabase('file:memory?mode=memory&cache=shared', uri=True)
else:
    mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        host=os.getenv("MYSQL_HOST"),
        port=3306
    )


print(mydb)
print(os.getenv("MYSQL_DATABASE"))
print(os.getenv("MYSQL_USER"))
print(os.getenv("MYSQL_PASSWORD"))
print(os.getenv("MYSQL_HOST"))



#creating the table
class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb


mydb.connect()
mydb.create_tables([TimelinePost])

# Variable declarations for texts
title = "Carlos Martínez - MLH Fellow"

photo = "./static/img/me.jpeg"

aboutMeGreetings = "Hello There! I'm Charlie"
aboutMeDescription = "I'm an MLH Fellow specializing in Production Engineering. I thrive on solving complex problems, optimizing systems, and ensuring the reliability and scalability of web applications. With a strong foundation in software engineering principles and hands-on experience in deploying and managing production systems, I am committed to delivering high-quality, efficient solutions."
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
        "title": "Software Engineer Intern",
        "company": "KATCON",
        "date": "October 2023 - Present",
        "description": "Deployed web applications using React to optimize internal processes of customer service and billing. Integrated AWS services on my projects to manage databases, authentication, and cloud storage. Developed a software solution to manage financial processes and received positive feedback from company leadership.",
        "image": "./static/img/katcon_logo.png"
    },
    {
        "id": 2,
        "title": "Founder Software Engineer",
        "company": "MedicFlow",
        "date": "December 2023 - April 2024",
        "description": "Developed the mobile application using React Native which is now the main product of the company. Led the Front-end development team and implemented Agile methodology to meet ambitious deadlines. Integrated AI models for speech recognition as well as LLMs for text processing.",
        "image": "./static/img/MF_logo.jpeg"
    },
    {
        "id": 3,
        "title": "Software Developer",
        "company": "Proyecto 99",
        "date": "December 2022 - February 2023",
        "description": "Developed a web application using React to manage their operations and allow students to sign up for courses. Learned about SCRUM methodology and software development processes. Deployed the project which is now used to manage student inscriptions.",
        "image": "./static/img/p99_logo.png"
    }

]
numOfJobs = len(workExperience)



hobbies = Hobbies(hobbies = [
  Hobby(
      title = "Playing Basketball with my friends",
      description = "I've always enjoyed playing sports with my friends but for the past couple years I've been playing basketball with my friends every saturday and it's been a blast!",
      images = [

          "./static/img/basketball.jpg"
      ]
  ),
  Hobby(
      title = "Playing the Piano",
      description = "Whenever i have time i love to play the piano, I've been slowly self teaching myself and it's been a great experience. I love learining new pices and get better and better evrey time i try a new one",
      images = [
          "./static/img/piano.jpg"
      ]
  ),
  Hobby(
      title = "Playing Video Games with my friends",
      description = "I always enjoy hanging out with my friends but usualy we don'get to see each other that often outside of school because we live far away from each other. However, we always play video games together like Valorant or lethal company it's a great way to keep in touch and have fun!",
      images = [
          "./static/img/steam.jpg",
      ]
  )
])

education = EducationHistory([
    EducationExperience(
        title = "Bachelor in Computer Science",
        school = "Tec de Monterrey",
        description = ["4.0/4.0 GPA", "Specialized Courses: Data Structures and algorithms, Software Construction, Computer Networks, Computacional Methods "],
        date = "2022 - 2026",
        logo = "https://upload.wikimedia.org/wikipedia/en/thumb/0/04/Utoronto_coa.svg/1280px-Utoronto_coa.svg.png"
    ),
    EducationExperience(
        title = "Multicultural High School Diploma",
        school = "Prepa Tec",
        description = ["3.7/4.0 GPA", "Specialized Courses: Advanced Calculus and Physics, French and introduction to Arduino"],
        date = "2019 - 2022",
        logo = "https://upload.wikimedia.org/wikipedia/en/thumb/0/04/Utoronto_coa.svg/1280px-Utoronto_coa.svg.png"
    ),
])

places_visited = PlacesVisited([
    PlaceVisited(
        title = "Paris, France",
        description = "A couple years ago i visited Paris with my family and it was super fun! We went to see the Eiffel Tower, Saint Chapelle and the castle of versailes",
        url = """https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2625.148689953084!2d2.3423859766072286!3d48.855374971331806!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x47e66e1fd8767d47%3A0x33f441f9dc242768!2sSainte%20Chapelle!5e0!3m2!1ses-419!2smx!4v1719261874308!5m2!1ses-419!2smx"""
    ),
    PlaceVisited(
        title = "Rome, Italy",
        description = "I also went to Rome for a week and it was amazing! I visited the Roman Coliseum, the fontana di trevi and a lot of beautiful churches that where several centuries old. I also went to the Roman Ruins and it was super intresting seeing all the ancient buildings still standing! My favorite part of Rome however was´t in Rome it was the Vatican where I saw the Sistine Chapel and the Basilica of Saint Peter. It was a super spiritual experience and I loved it!",
        url = """https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d658.6749338764339!2d12.482714570913103!3d41.90084105214406!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x132f6053278340d5%3A0xf676f1e1cc02bbb6!2sFontana%20di%20Trevi!5e0!3m2!1ses-419!2smx!4v1719262442457!5m2!1ses-419!2smx"""
    ),
    PlaceVisited(
        title = "Florence, Italy",
        description = "One of my favorite places in Europe is the Basilica de Santa Maria del Fiore, I went there with my familly and when we saw the facade we just stood there forever. The detail in this church and the whole building makes it an architectural wonder. I also went to several other churches and museums in Florence and it was a great experience!",
        url = "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d1347.7494125042347!2d11.25471911221566!3d43.77316970881967!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x132a5403bfe22ff5%3A0x5591438487aaf1f5!2sCatedral%20de%20Santa%20Mar%C3%ADa%20del%20Fiore!5e0!3m2!1ses-419!2smx!4v1719262814961!5m2!1ses-419!2smx"
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


@app.route('/hobbies_page')
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
@app.route('/timeline')
def timeline():
    return render_template(
        'timeline.html',
        title = "MLH Fellow",
        photo = photo,
        url=os.getenv("URL"),
        posts=get_timeline_post()

    )



# API Endpoints

@app.route('/api/timeline_post', methods=['POST'])
def post_timeline_post():
    name = request.form.get('name')
    if name is None:
        return {"error": "Invalid name"}, 400

    email = request.form.get('email')
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if email is None or not re.match(email_regex, email):
        return {"error": "Invalid email"}, 400

    content = request.form.get('content')
    if content is None or len(content) == 0:
        return {"error": "Invalid content"}, 400

    # Create and return the timeline post
    timeline_post = TimelinePost.create(name=name, email=email, content=content)
    return model_to_dict(timeline_post)

@app.route('/api/timeline_post', methods=['GET'])
def get_timeline_post():
    return {
        'timeline_posts': [
            model_to_dict(p)
            for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }

@app.route('/api/timeline_post', methods=['DELETE'])
def delete_timeline_post():
    post_id = request.form['id']
    print(post_id)
    TimelinePost.delete().where(TimelinePost.id == post_id).execute()

    return {

        'Message': "Post deleted successfully!"
    }
