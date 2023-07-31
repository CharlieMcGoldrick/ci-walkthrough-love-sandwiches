# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread #import all of gspread
from google.oauth2.service_account import Credentials  #import Credentials class

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

#  Call the from_service_account method from Credentials class
CREDS = Credentials.from_service_account_file('creds.json')
#  Pass the with_scopes method to the CREDS object  
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
#  Use gspread.authorize method
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
#  Use the open method to access love_sandwhiches sheet
SHEET = GSPREAD_CLIENT.open('love_sandwiches') 

#  Call Sales worksheet
sales = SHEET.worksheet('sales')

#  gspread method to get all of the values
data = sales.get_all_values()


def get_sales_data():
    """
    Get sales figures input from the user
    """
    print("Please enter sales data from the last market.")
    print("Data should be six numbers.")
    print("Example: 10,20,30,40,50,60\n")

    data_str = input("Enter your data here: ")
    print(f"The data provided is {data_str}")


get_sales_data()