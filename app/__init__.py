import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

# Variable declarations for texts
title = "MLH Fellow"
aboutMeGreetings = "Hello There! I'm Charlie"
aboutMeDescription = "I'm a passionate and dedicated MLH Fellow specializing in Production Engineering. I thrive on solving complex problems, optimizing systems, and ensuring the reliability and scalability of web applications. With a strong foundation in software engineering principles and hands-on experience in deploying and managing production systems, I am committed to delivering high-quality, efficient solutions."
workExperience = [
    {
        "id": 0,
        "title": "MLH Production Engineer Fellow",
        "company": "Major League Hacking",
        "date": "June 2024 - Present",
        "description": "Participated in a fellowship program focused on site reliability engineering and DevOps. Implemented CI/CD pipelines, monitored system performance, and collaborated with a global team to improve application scalability and reliability.",
        "image": "path/to/mlh_image.jpg"
    },
    {
        "id": 1,
        "title": "Software Engineer Intern",
        "company": "KATCON",
        "date": "October 2023 - Present",
        "description": "Deployed web applications using React to optimize internal processes of customer service and billing. Integrated AWS services on my projects to manage databases, authentication, and cloud storage. Developed a software solution to manage financial processes and received positive feedback from company leadership.",
        "image": "path/to/katcon_image.jpg"
    },
    {
        "id": 2,
        "title": "Founder Software Engineer",
        "company": "MedicFlow",
        "date": "December 2023 - April 2024",
        "description": "Developed the mobile application using React Native which is now the main product of the company. Led the Front-end development team and implemented Agile methodology to meet ambitious deadlines. Integrated AI models for speech recognition as well as LLMs for text processing.",
        "image": "path/to/medicflow_image.jpg"
    },
    {
        "id": 3,
        "title": "Software Developer",
        "company": "Proyecto 99",
        "date": "December 2022 - February 2023",
        "description": "Developed a web application using React to manage their operations and allow students to sign up for courses. Learned about SCRUM methodology and software development processes. Deployed the project which is now used to manage student inscriptions.",
        "image": "path/to/proyecto99_image.jpg"
    }

]
numOfJobs = len(workExperience)


@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", aboutMeGreetings=aboutMeGreetings, aboutMeDescription=aboutMeDescription,  workExperience=workExperience, numOfJobs=numOfJobs, url=os.getenv("URL"))
