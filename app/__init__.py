import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from app.hobby import Hobbies, Hobby
from app.education import EducationExperience, EducationHistory

load_dotenv()
app = Flask(__name__)

# Variable declarations for texts
title = "MLH Fellow"
aboutMeGreetings = "Hello There! I'm Charlie"
aboutMeDescription = "I'm a passionate and dedicated MLH Fellow specializing in Production Engineering. I thrive on solving complex problems, optimizing systems, and ensuring the reliability and scalability of web applications. With a strong foundation in software engineering principles and hands-on experience in deploying and managing production systems, I am committed to delivering high-quality, efficient solutions."


hobbies = Hobbies(hobbies = [
  Hobby(
      title = "Underwater basket weaving",
      description = "Every weekend, I weave baskets underwater",
      images = [
          "https://letsenhance.io/static/8f5e523ee6b2479e26ecc91b9c25261e/1015f/MainAfter.jpg"
      ]
  ), 
  Hobby(
      title = "Underwater basket weaving 2",
      description = "Every weekend, I weave baskets underwater",
      images = [
          "https://letsenhance.io/static/8f5e523ee6b2479e26ecc91b9c25261e/1015f/MainAfter.jpg"
      ]
  ),
  Hobby(
      title = "Underwater basket weaving 3",
      description = "Every weekend, I weave baskets underwater",
      images = [
          "https://letsenhance.io/static/8f5e523ee6b2479e26ecc91b9c25261e/1015f/MainAfter.jpg"
      ]
  )
])

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
        hobbies = hobbies,
        education = education,
        url=os.getenv("URL")
    )
