import pandas as pd
import os
data  = pd.read_csv(r"D:\Number Plate Recogniton\output.csv")

path = data['Path']
real = data['Real']
pred = data['Predicted']

directory = 'USABLE_DATA'
files_in_directory = os.listdir(directory)



for filename in files_in_directory:
        # # Construct the full path to the file
        file_path = os.path.join(directory, filename)
        
        
        if filename not in list(path):
            # If the file is not in the list, remove it
            os.remove(file_path)
            print(f"Removed: {filename}")
        else:
            print(f"Kept: {filename}")














# import os

# def keep_files(directory, filenames_to_keep):
#     # Get the list of all files in the directory
#     files_in_directory = os.listdir(directory)
#     print(files_in_directory)
#     # Iterate through the files in the directory
#     for filename in files_in_directory:
#         # Construct the full path to the file
#         file_path = os.path.join(directory, filename)
        
#         # Check if the current file is in the list of filenames to keep
#         if filename not in filenames_to_keep:
#             # If the file is not in the list, remove it
#             #os.remove(file_path)
#             print(f"Removed: {filename}")
#         else:
#             print(f"Kept: {filename}")


# directory = 'USABLE_DATA'


# # Call the function
# keep_files(directory, path)
