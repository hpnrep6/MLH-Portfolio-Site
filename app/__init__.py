import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from app.education import EducationExperience, EducationHistory

load_dotenv()
app = Flask(__name__)

# Variable declarations for texts
title = "MLH Fellow"
aboutMeGreetings = "Hello There! I'm Charlie"
aboutMeDescription = "I'm a passionate and dedicated MLH Fellow specializing in Production Engineering. I thrive on solving complex problems, optimizing systems, and ensuring the reliability and scalability of web applications. With a strong foundation in software engineering principles and hands-on experience in deploying and managing production systems, I am committed to delivering high-quality, efficient solutions."

education = EducationHistory([
    EducationExperience(
        title = "Bachelor of Science in Computer Science",
        school = "University of Toronto",
        description = ["X/4.0 GPA", "Awards: Placeholder awards"],
        date = "2021 - 2025",
        logo = "https://upload.wikimedia.org/wikipedia/en/thumb/0/04/Utoronto_coa.svg/1280px-Utoronto_coa.svg.png"
    ), 
    EducationExperience(
        title = "Ontario Secondary School Degree (OSSD)",
        school = "Some High School I guess",
        description = ["X/4.0 GPA", "Awards: Placeholder awards"],
        date = "2017 - 2021",
        logo = "https://upload.wikimedia.org/wikipedia/en/thumb/0/04/Utoronto_coa.svg/1280px-Utoronto_coa.svg.png"
    ), 
])

@app.route('/')
def index():
    return render_template(
        'index.html', 
        title="MLH Fellow", 
        aboutMeGreetings=aboutMeGreetings, 
        aboutMeDescription=aboutMeDescription, 
        education = education,
        url=os.getenv("URL")
    )
