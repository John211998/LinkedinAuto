from dotenv import load_dotenv
import os
import yaml

# Load environment variables from .env file
load_dotenv()

# Retrieve sensitive information from environment variables
api_key = os.getenv('API_KEY')
password = os.getenv('PASSWORD')
mail = os.getenv('MAIL')

# Define the data to be used in your YAML configuration
data = {
    'email': mail,
    'password': password,
    'openai_api_key': api_key
}


# Write the data to the YAML file
with open('data_folder/secrets.yaml', 'w') as file:
    yaml.dump(data, file, default_flow_style=False)

print("YAML file has been updated successfully.")
