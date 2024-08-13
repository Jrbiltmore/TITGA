
# compliance_checker.py

import logging

# Configure logging
logging.basicConfig(filename='/mnt/data/TIGTA_Automation_Suite/Compliance/Logs/compliance_audit.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def check_compliance(data, rules):
    """
    Checks the provided data against the specified compliance rules.
    Args:
        data (dict): The data to be checked for compliance.
        rules (dict): A dictionary of compliance rules to apply.
    Returns:
        list: A list of compliance violations found, or an empty list if none are found.
    """
    violations = []

    try:
        for rule_name, rule_function in rules.items():
            if not rule_function(data):
                violations.append(f"Violation of {rule_name}")

        if violations:
            logging.info(f"Compliance violations found: {violations}")
            print(f"Compliance violations found: {violations}")
        else:
            logging.info("No compliance violations found.")
            print("No compliance violations found.")

        return violations

    except Exception as e:
        logging.error(f"Error in compliance checking: {e}")
        print(f"Error: {e}")
        return ["Error in compliance checking"]

# Example compliance rule
def example_rule(data):
    return data.get('transaction_amount', 0) <= 100000

# Example usage
if __name__ == "__main__":
    example_data = {'transaction_amount': 150000}
    example_rules = {'Transaction Limit': example_rule}
    violations = check_compliance(example_data, example_rules)
    print(violations)
