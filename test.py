import gspread
from oauth2client.service_account import ServiceAccountCredentials


# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("Account Development").sheet1

# Extract and print all of the values in list of hashes
list_of_hashes = sheet.get_all_records()

# Extract and print all of the values in list of lists
list_of_lists = sheet.get_all_values()

# Extract data from single row
one_row = sheet.row_values(1)

# Extract data from single column
one_column = sheet.col_values(1)

# Extract data from single cell
one_cell = sheet.cell(1,1).value

# Write to a cell
sheet.update_cell(1,1, "hello world")

# Insert a row at index 1
row = ["i", "am", "inserting", "a", "row"]
index = 1
sheet.insert_row(row, index)

# Delete a row
sheet.delete_row(2)

# Count number of rows
print(sheet.row_count)