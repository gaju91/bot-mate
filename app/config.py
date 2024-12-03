from dotenv import load_dotenv
import os

load_dotenv()

# OpenAI API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Sanity CMS Configuration
SANITY_PROJECT_ID = os.getenv("SANITY_PROJECT_ID")
SANITY_API_TOKEN = os.getenv("SANITY_API_TOKEN")
SANITY_BASE_URL = f"https://{SANITY_PROJECT_ID}.api.sanity.io/v1/data/query/development"
