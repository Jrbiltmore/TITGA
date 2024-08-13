
# trend_analysis.py

import logging
import pandas as pd
import matplotlib.pyplot as plt

# Configure logging
logging.basicConfig(filename='/mnt/data/TIGTA_Automation_Suite/DataAnalytics/Logs/data_import.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def analyze_trends(dataset_path, output_path):
    """
    Analyzes trends in the given dataset and generates a visual report.
    Args:
        dataset_path (str): Path to the dataset file.
        output_path (str): Path where the trend report (e.g., plots) will be saved.
    Returns:
        bool: True if analysis is successful, False otherwise.
    """
    try:
        # Load the dataset
        data = pd.read_csv(dataset_path)
        
        # Example trend analysis: Plotting trends over time (if time series data is available)
        if 'date' in data.columns:
            data['date'] = pd.to_datetime(data['date'])
            data.set_index('date', inplace=True)
            trend_data = data.resample('M').sum()

            # Plotting
            plt.figure(figsize=(10, 6))
            plt.plot(trend_data.index, trend_data['transaction_amount'], marker='o', linestyle='-')
            plt.title('Monthly Trend of Transaction Amounts')
            plt.xlabel('Date')
            plt.ylabel('Total Transaction Amount')
            plt.grid(True)
            plt.savefig(output_path)
            plt.close()

            logging.info(f"Trend analysis completed and report saved to {output_path}.")
            print(f"Trend analysis completed and report saved to {output_path}.")
            return True
        else:
            logging.warning(f"Dataset {dataset_path} does not contain 'date' column. Trend analysis skipped.")
            print(f"Dataset {dataset_path} does not contain 'date' column. Trend analysis skipped.")
            return False

    except Exception as e:
        logging.error(f"Error in trend analysis: {e}")
        print(f"Error: {e}")
        return False

# Example usage
if __name__ == "__main__":
    analyze_trends('/mnt/data/TIGTA_Automation_Suite/DataAnalytics/Datasets/fraud_cases.csv', 
                   '/mnt/data/TIGTA_Automation_Suite/DataAnalytics/Reports/trend_report.png')
