from dotenv import load_dotenv
import os
import requests

load_dotenv()

def fetch_data(animal_name):
  """Fetches animal data from the API Ninja Animals API."""
  api_key = os.getenv("API_KEY")
  if not api_key:
      print("Error: API_KEY not found in .env file")
      return None

  url = f"https://api.api-ninjas.com/v1/animals?name={animal_name}"
  headers = {'X-Api-Key': api_key}

  try:
      response = requests.get(url, headers=headers)
      response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
      return response.json()
  except requests.exceptions.RequestException as e:
      print(f"An error occurred: {e}")
      return None