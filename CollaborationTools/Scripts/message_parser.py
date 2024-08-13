
# message_parser.py

import logging

# Configure logging
logging.basicConfig(filename='/mnt/data/TIGTA_Automation_Suite/CollaborationTools/Logs/collaboration.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def parse_message(message):
    """
    Parses a message to extract key information.
    Args:
        message (str): The message text to parse.
    Returns:
        dict: A dictionary containing the parsed information.
    """
    try:
        # Example parsing logic
        parsed_data = {
            'length': len(message),
            'words': message.split(),
            'word_count': len(message.split())
        }

        logging.info(f"Message parsed: {parsed_data}")
        print(f"Message parsed: {parsed_data}")
        return parsed_data

    except Exception as e:
        logging.error(f"Error in parsing message: {e}")
        print(f"Error: {e}")
        return {}

# Example usage
if __name__ == "__main__":
    example_message = "This is an example message for parsing."
    parse_message(example_message)
