
# data_analysis.py

import logging
import pandas as pd

# Configure logging
logging.basicConfig(filename='/mnt/data/TIGTA_Automation_Suite/DataAnalytics/Logs/analytics.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def analyze_data(dataset_path):
    """
    Analyzes the given dataset and provides summary statistics and insights.
    Args:
        dataset_path (str): Path to the dataset file.
    Returns:
        pd.DataFrame: A DataFrame containing summary statistics.
    """
    try:
        # Load the dataset
        data = pd.read_csv(dataset_path)
        
        # Perform basic analysis
        summary_stats = data.describe()
        
        # Log the analysis
        logging.info(f"Data analysis completed for {dataset_path}. Summary statistics generated.")
        print(f"Data analysis completed for {dataset_path}. Summary statistics generated.")
        
        return summary_stats

    except Exception as e:
        logging.error(f"Error in data analysis: {e}")
        print(f"Error: {e}")
        return pd.DataFrame()

# Example usage
if __name__ == "__main__":
    summary = analyze_data('/mnt/data/TIGTA_Automation_Suite/DataAnalytics/Datasets/fraud_cases.csv')
    print(summary)
