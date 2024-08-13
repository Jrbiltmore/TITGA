
# document_uploader.py

import logging
import os
from shutil import copyfile

# Configure logging
logging.basicConfig(filename='/mnt/data/TIGTA_Automation_Suite/DocumentManagement/Logs/storage.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def upload_document(source_path, destination_directory):
    """
    Uploads a document to the specified storage directory.
    Args:
        source_path (str): The file path of the document to upload.
        destination_directory (str): The directory where the document will be stored.
    Returns:
        bool: True if the upload is successful, False otherwise.
    """
    try:
        if not os.path.exists(destination_directory):
            os.makedirs(destination_directory)

        destination_path = os.path.join(destination_directory, os.path.basename(source_path))
        copyfile(source_path, destination_path)

        logging.info(f"Document uploaded to {destination_path}.")
        print(f"Document uploaded to {destination_path}.")
        return True

    except Exception as e:
        logging.error(f"Error in uploading document: {e}")
        print(f"Error: {e}")
        return False

# Example usage
if __name__ == "__main__":
    upload_document('/mnt/data/TIGTA_Automation_Suite/DocumentManagement/Docs/ExampleDoc.txt', 
                    '/mnt/data/TIGTA_Automation_Suite/DocumentManagement/Storage/case_documents/')
