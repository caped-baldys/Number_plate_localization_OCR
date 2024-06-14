import csv

# Define the CSV file name
csv_file_name = 'output.csv'

# Define the headers for the CSV file
headers = ['Path','Real','Predicted']  # Adjust these as needed

# Open the CSV file in write mode and create a CSV writer object
with open(csv_file_name, mode='a', newline='') as file:
    writer = csv.writer(file)
    
    # Write the headers to the CSV file

    writer.writerow(headers)
    
    while True:
        # Prompt the user for data input
        row_data = []
        for header in headers:
            data = input(f"Enter data for {header}: ")
            if data.lower() == 'x':
                print("Exiting and saving the CSV file.")
                exit()
            row_data.append(data)
        
        # Write the row data to the CSV file
        writer.writerow(row_data)
        print("\n")
