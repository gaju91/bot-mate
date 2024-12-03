import requests
from app.config import SANITY_BASE_URL, SANITY_API_TOKEN

def fetch_services():
    """
    Fetches all services from Sanity CMS.
    Returns a string formatted for AI model input.
    """
    query = '*[_type == "division"]{divisionName, shortDescription}'
    headers = {"Authorization": f"Bearer {SANITY_API_TOKEN}"}
    
    response = requests.get(f"{SANITY_BASE_URL}?query={query}", headers=headers)
    
    if response.status_code != 200:
        raise Exception(f"Error fetching data from Sanity: {response.text}")
    
    data = response.json()
    return "\n".join([f"{item['divisionName']}: {item['shortDescription']}" for item in data["result"]])
