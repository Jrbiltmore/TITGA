
# audit_report_generator.py

import logging
import datetime

# Configure logging
logging.basicConfig(filename='/mnt/data/TIGTA_Automation_Suite/AuditCompliance/Logs/audit.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def generate_audit_report(audit_data, report_path):
    """
    Generates an audit report based on the provided audit data.
    Args:
        audit_data (dict): A dictionary containing audit findings and details.
        report_path (str): The file path where the report will be saved.
    Returns:
        bool: True if the report is generated successfully, False otherwise.
    """
    try:
        report_content = f"Audit Report - {datetime.datetime.now().strftime('%Y-%m-%d')}
"
        report_content += "=" * 40 + "
"

        for key, value in audit_data.items():
            report_content += f"{key}: {value}
"

        with open(report_path, 'w') as report_file:
            report_file.write(report_content)

        logging.info(f"Audit report generated and saved to {report_path}.")
        print(f"Audit report generated and saved to {report_path}.")
        return True

    except Exception as e:
        logging.error(f"Error in generating audit report: {e}")
        print(f"Error: {e}")
        return False

# Example usage
if __name__ == "__main__":
    audit_example = {
        'Audit ID': 12345,
        'Auditor': 'Jane Doe',
        'Findings': 'No significant issues found.',
        'Recommendations': 'Continue current practices.',
        'Date': '2024-08-13'
    }
    generate_audit_report(audit_example, '/mnt/data/TIGTA_Automation_Suite/AuditCompliance/Reports/audit_report_2024.pdf')
