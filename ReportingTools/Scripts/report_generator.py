
# report_generator.py

import logging
import os
import pdfkit

# Configure logging
logging.basicConfig(filename='/mnt/data/TIGTA_Automation_Suite/ReportingTools/Logs/reporting.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def generate_report(report_data, output_path):
    """
    Generates a report in PDF format using the provided data.
    Args:
        report_data (dict): A dictionary containing report details.
        output_path (str): The file path where the report will be saved.
    Returns:
        bool: True if the report is generated successfully, False otherwise.
    """
    try:
        # Simple HTML template for the report
        html_content = f"""
        <html>
        <head><title>{report_data['title']}</title></head>
        <body>
        <h1>{report_data['title']}</h1>
        <p><strong>Date:</strong> {report_data['date']}</p>
        <p><strong>Author:</strong> {report_data['author']}</p>
        <hr>
        <p>{report_data['content']}</p>
        </body>
        </html>
        """

        # Convert HTML to PDF
        pdfkit.from_string(html_content, output_path)

        logging.info(f"Report generated and saved to {output_path}.")
        print(f"Report generated and saved to {output_path}.")
        return True

    except Exception as e:
        logging.error(f"Error in generating report: {e}")
        print(f"Error: {e}")
        return False

# Example usage
if __name__ == "__main__":
    example_report_data = {
        'title': 'Monthly Audit Report',
        'date': '2024-08-13',
        'author': 'John Doe',
        'content': 'This report summarizes the audit findings for the month of August 2024.'
    }
    generate_report(example_report_data, '/mnt/data/TIGTA_Automation_Suite/ReportingTools/Reports/monthly_report_2024.pdf')
