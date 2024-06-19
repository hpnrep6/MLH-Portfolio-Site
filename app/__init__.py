import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from app.hobby import Hobbies, Hobby

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

@app.route('/')
def index():
    return render_template(
        'index.html', 
        title="MLH Fellow", 
        aboutMeGreetings=aboutMeGreetings, 
        aboutMeDescription=aboutMeDescription,
        hobbies = hobbies,
        url=os.getenv("URL")
      )
