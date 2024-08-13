
# api_handler.py

import logging
import requests

# Configure logging
logging.basicConfig(filename='/mnt/data/TIGTA_Automation_Suite/IntegrationAPI/Logs/api_requests.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def make_api_request(endpoint, headers=None, params=None):
    """
    Makes an API request to the specified endpoint.
    Args:
        endpoint (str): The API endpoint URL.
        headers (dict): Optional headers to include in the request.
        params (dict): Optional query parameters to include in the request.
    Returns:
        dict: The JSON response from the API, or None if an error occurs.
    """
    try:
        response = requests.get(endpoint, headers=headers, params=params)
        response.raise_for_status()  # Raise an error for bad status codes
        logging.info(f"API request to {endpoint} successful.")
        print(f"API request to {endpoint} successful.")
        return response.json()

    except requests.exceptions.HTTPError as http_err:
        logging.error(f"HTTP error occurred: {http_err}")
        print(f"HTTP error occurred: {http_err}")
        return None

    except Exception as e:
        logging.error(f"Error in making API request: {e}")
        print(f"Error: {e}")
        return None

# Example usage
if __name__ == "__main__":
    example_endpoint = "https://api.example.com/data"
    response_data = make_api_request(example_endpoint)
    print(response_data)
