
# Import the necessary modules
from github import Github
import requests
import os

# Authenticate with GitHub
ACCESS_TOKEN = "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"
g = Github(ACCESS_TOKEN)

# Get the repository and file
repo = g.get_repo("Nathwoo/20210031")
file = repo.get_contents('reponseAPI.txt')

#Get latitude and longitude 
LATITUDE = os.environ.get('LATITUDE')
LONGITUDE = os.environ.get('LONGITUDE')

# Make an API call to OpenWeather
url = "https://api.openweathermap.org/data/2.5/weather?lat={LATITUDE}&lon={LONGITUDE}&appid=a6df1754733f5fef4256026cf2921a3c"
response = requests.get(url)

# Update the file with the new content
file_content = response.content
commit_message = "Update file with new content"
repo.update_file(file.path, commit_message, file_content, file.sha)
