import pandas as pd
import os

# Input and output paths
input_csv = 'annotated_kamala_harris_articles.csv'  # Replace with your CSV file name
output_dir = 'categories'  # Directory where category-specific files will be saved

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Load the CSV file into a DataFrame
df = pd.read_csv(input_csv)

#Clean columns in order to not consider a difference between like Campaign.csv and Campaign .csv 
df.columns = df.columns.str.strip()
df['Annotation'] = df['Annotation'].str.strip()

# Check if the 'Annotation' column exists
if 'Annotation' not in df.columns:
    raise ValueError("The 'Annotation' column is missing from the CSV file.")

# Group by the 'Annotation' column
for category, group in df.groupby('Annotation'):
    # Replace invalid characters in category names for filenames
    safe_category = "".join(c if c.isalnum() or c in (" ", "_", "-") else "_" for c in category)
    output_file = os.path.join(output_dir, f"{safe_category}.csv")
    
    # Save each category group to a separate CSV
    group.to_csv(output_file, index=False)
    print(f"Saved {len(group)} articles to {output_file}")