import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API key
api_key = os.getenv("API_KEY")

# Print API key
print(f"API Key: {api_key}")
