
# Import the necessary modules
import requests
import os

#Get latitude, longitude and API key
LATITUDE = os.environ.get('LAT')
LONGITUDE = os.environ.get('LONG')
KEY = os.environ.get('API_KEY')

# Make an API call to OpenWeather
url = f'https://api.openweathermap.org/data/2.5/weather?lat={LATITUDE}&lon={LONGITUDE}&appid={KEY}&units=metric'
response = requests.get(url)

# Update the file with the new content
file_content = response.content
print(file_content)
