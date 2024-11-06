import os
import pandas as pd

# Define the folder path
folder_path = 'manul/data/res_clean_8b'

file_data_list = []

# Iterate through all files in the folder
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    
    # Check if the file is a .txt file
    if filename.endswith('.txt'):
        # Read the text file as a single string
        with open(file_path, 'r') as file:
            file_content = file.read()
        
        # Append a dictionary with filename and content to the list
        file_data_list.append({'content': file_content})
        print(f"opened: {filename} ")
    else:
        print(f"Skipping unsupported file: {filename}")

# Convert the list of dictionaries into a DataFrame
combined_data = pd.DataFrame(file_data_list)

# Save the combined data to a CSV file (if you still want a CSV)
output_file = 'combined_data.csv'
combined_data.to_csv(output_file, index=False)


print(f"All data combined and saved to {output_file}")