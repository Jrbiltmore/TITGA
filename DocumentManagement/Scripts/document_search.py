
# document_search.py

import logging
import os

# Configure logging
logging.basicConfig(filename='/mnt/data/TIGTA_Automation_Suite/DocumentManagement/Logs/document_access.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def search_document(search_term, storage_directory):
    """
    Searches for documents in the specified storage directory that match the search term.
    Args:
        search_term (str): The term to search for in document filenames.
        storage_directory (str): The directory where documents are stored.
    Returns:
        list: A list of file paths that match the search term.
    """
    try:
        matching_files = []
        for root, dirs, files in os.walk(storage_directory):
            for file in files:
                if search_term.lower() in file.lower():
                    matching_files.append(os.path.join(root, file))

        if matching_files:
            logging.info(f"Found {len(matching_files)} matching documents for '{search_term}' in {storage_directory}.")
            print(f"Found {len(matching_files)} matching documents for '{search_term}' in {storage_directory}.")
        else:
            logging.info(f"No matching documents found for '{search_term}' in {storage_directory}.")
            print(f"No matching documents found for '{search_term}' in {storage_directory}.")

        return matching_files

    except Exception as e:
        logging.error(f"Error in searching documents: {e}")
        print(f"Error: {e}")
        return []

# Example usage
if __name__ == "__main__":
    results = search_document('ExampleDoc', '/mnt/data/TIGTA_Automation_Suite/DocumentManagement/Storage/case_documents/')
    print(results)
