class EducationExperience:
  title = ""
  school = ""
  description = []
  date = ""
  logo = ""
  
  def __init__(self, title, school, description, date, logo):
    self.title = title
    self.school = school
    self.description = description
    self.date = date
    self.logo = logo
  
class EducationHistory:
  experiences = []
  
  def __init__(self, experiences):
    self.experiences = experiences