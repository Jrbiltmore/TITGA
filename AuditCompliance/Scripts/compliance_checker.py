
# compliance_checker.py

import logging

# Configure logging
logging.basicConfig(filename='/mnt/data/TIGTA_Automation_Suite/AuditCompliance/Logs/compliance.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def check_compliance(case_data, compliance_rules):
    """
    Checks a case against compliance rules and identifies any violations.
    Args:
        case_data (dict): A dictionary containing case details.
        compliance_rules (dict): A dictionary containing compliance rules.
    Returns:
        list: A list of compliance violations, if any.
    """
    violations = []
    
    try:
        for rule, criteria in compliance_rules.items():
            if not criteria(case_data):
                violations.append(f"Violation of {rule}")

        if violations:
            logging.info(f"Compliance violations found in case {case_data['case_id']}: {violations}")
            print(f"Compliance violations found in case {case_data['case_id']}: {violations}")
        else:
            logging.info(f"Case {case_data['case_id']} is compliant.")
            print(f"Case {case_data['case_id']} is compliant.")
        
        return violations

    except Exception as e:
        logging.error(f"Error in compliance checking: {e}")
        print(f"Error: {e}")
        return ["Error in compliance checking"]

# Example compliance rule
def example_compliance_rule(case_data):
    return case_data.get('financial_impact', 0) <= 100000

# Example usage
if __name__ == "__main__":
    case_example = {
        'case_id': 12345,
        'financial_impact': 150000,
        'severity': 'High'
    }
    compliance_rules_example = {
        'Financial Impact Rule': example_compliance_rule
    }
    check_compliance(case_example, compliance_rules_example)
