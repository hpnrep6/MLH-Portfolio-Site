class PlaceVisited:
  title = ""
  description = ""

  # Get the URL from https://www.maps.ie/create-google-map/ for the iFrame
  url = ""

  def __init__(self, title, description, url):
    self.title = title
    self.description = description
    self.url = url

class PlacesVisited:
  places = []

  def __init__(self, places):
    self.places = places