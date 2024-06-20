class Hobby:
  title = ""
  description = ""
  images = []

  def __init__(self, title, description, images):
    self.title = title
    self.description = description
    self.images = images

class Hobbies:
  hobbies = []

  def __init__(self, hobbies):
    self.hobbies = hobbies