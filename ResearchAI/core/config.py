import os
from dotenv import load_dotenv
from openai import AzureOpenAI

# Load environment variables
load_dotenv()

# Azure OpenAI configuration
client = AzureOpenAI(
    api_key=os.getenv("AZURE_API_KEY"),
    azure_endpoint=os.getenv("AZURE_ENDPOINT"),
    api_version=os.getenv("AZURE_API_VERSION")
)

# Google Search configuration
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GOOGLE_CX = os.getenv("GOOGLE_CX")

# Model configuration
MODEL_NAME = "gpt-4.1-nano"
MAX_TOKENS = 2000
MAX_ITERATIONS = 10