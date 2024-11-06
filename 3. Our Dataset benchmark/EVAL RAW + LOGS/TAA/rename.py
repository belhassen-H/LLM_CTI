import os

# Define the folder path
folder_path = 'manul/clean/res_clean_70b'

# Iterate through all files in the folder
for filename in os.listdir(folder_path):
    # Construct the full old file path
    old_file_path = os.path.join(folder_path, filename)
    
    # Skip directories and only rename files
    if os.path.isfile(old_file_path):
        # Split the name and extension
        name, ext = os.path.splitext(filename)
        
        # Ensure the filename has at least 5 characters to apply the transformation
        if len(name) >= 5:
            # Move the 4th and 5th characters to the start of the filename
            new_name = name[3:5] + name[:3] + name[5:]
        else:
            # If the filename is too short, keep it unchanged
            new_name = name
        
        # Construct the new filename with the transformed name and original extension
        new_filename = f"{new_name}{ext}"
        
        # Construct the full new file path
        new_file_path = os.path.join(folder_path, new_filename)
        
        # Rename the file
        os.rename(old_file_path, new_file_path)
        
        print(f"Renamed: {filename} to {new_filename}")

print("All files have been renamed.")