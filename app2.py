import os
from joblib import load

# Define the directory path where the joblib files are located
directory = "C:/Users/mrpai/OneDrive/Desktop"

# Load the joblib files from the specified directory
popular_df = load(os.path.join(directory, 'popular5.joblib'))
pt = load(os.path.join(directory, 'pt5.joblib'))
books = load(os.path.join(directory, 'books5.joblib'))
similarity_scores = load(os.path.join(directory, 'similarity_scores5.joblib'))