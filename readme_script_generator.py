# This script generates Markdown documentation from the OpenAPI spec.

import  requests
import subprocess
import os

# Configuration
FLASK_APP_URL = "http://localhost:5000/openapi.json"  # Update if needed
SPEC_FILE = "openapi.json"
OUTPUT_DIR = "api_docs"

def fetch_openapi_spec():
    """Fetch the OpenAPI specification from the Flask app."""
    try:
        response = requests.get(FLASK_APP_URL)
        response.raise_for_status()
        with open(SPEC_FILE, 'w') as file:
            file.write(response.text)
        print(f"OpenAPI specification saved to {SPEC_FILE}")
    except requests.RequestException as e:
        print(f"Error fetching OpenAPI spec: {e}")
        exit(1)

def generate_markdown():
    """Generate Markdown documentation from the OpenAPI spec."""
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    
    try:
        subprocess.run([
            "openapi-generator", "generate",
            "-i", SPEC_FILE,
            "-g", "markdown",
            "-o", OUTPUT_DIR
        ], check=True)
        print(f"Markdown documentation generated in {OUTPUT_DIR}")
    except subprocess.CalledProcessError as e:
        print(f"Error generating Markdown: {e}")
        exit(1)

def main():
    fetch_openapi_spec()
    generate_markdown()

if __name__ == "__main__":
    main()
