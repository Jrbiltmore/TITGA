
# prioritization.py

import logging

# Configure logging
logging.basicConfig(filename='/mnt/data/TIGTA_Automation_Suite/CaseManagement/Logs/prioritization.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def prioritize_case(case_data):
    """
    Determines the priority level of a case based on various criteria such as severity, financial impact, and involved parties.
    Args:
        case_data (dict): A dictionary containing case details.
    Returns:
        str: The priority level of the case ('High', 'Medium', 'Low').
    """
    try:
        # Example prioritization logic
        financial_impact = case_data.get('financial_impact', 0)
        severity = case_data.get('severity', 'Low')

        if financial_impact > 100000 or severity == 'High':
            priority_level = 'High'
        elif financial_impact > 10000 or severity == 'Medium':
            priority_level = 'Medium'
        else:
            priority_level = 'Low'

        logging.info(f"Case {case_data['case_id']} prioritized as {priority_level}.")
        print(f"Case {case_data['case_id']} prioritized as {priority_level}.")
        return priority_level

    except Exception as e:
        logging.error(f"Error in case prioritization: {e}")
        print(f"Error: {e}")
        return 'Low'

# Example usage
if __name__ == "__main__":
    case_example = {
        'case_id': 12345,
        'financial_impact': 50000,
        'severity': 'Medium'
    }
    prioritize_case(case_example)
